#!/usr/bin/env python3
"""Generate a brand-styled illustration via Google Gemini (Nano Banana Pro).

This is the generation engine behind the `generate-image` skill. It is
brand-agnostic: the brand "look" lives in your prompt, which the skill builds
from brand/guidelines.md + brand/tokens.css before calling this script. The
script just sends the prompt (plus any reference images) to the Gemini image
API, saves the PNG, and writes a JSON sidecar journaling exactly what was sent
so the result is reproducible and auditable.

Usage:
    python3 scripts/gen-image.py --slug <slug> --prompt-file <path> \
        [--ref ref1.png ref2.png ...] [--aspect 16:9]

Credentials are read from a `.env` file at the repo root (git-ignored):
    GOOGLE_AI_API_KEY=...                       # required
    GOOGLE_AI_IMAGE_MODEL=gemini-3-pro-image-preview   # optional, this is the default

Real environment variables, when set, take precedence over `.env`.

Output:
    assets/illustrations/YYYY-MM-DD-<slug>.png   (the image)
    assets/illustrations/YYYY-MM-DD-<slug>.json  (sidecar: prompt + metadata)
"""
import argparse
import base64
import datetime
import json
import mimetypes
import os
import pathlib
import sys

try:
    import requests
except ImportError:
    sys.exit(
        "ERROR: the `requests` package is required.\n"
        "Install it with:  python3 -m pip install requests"
    )

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "assets" / "illustrations"
DEFAULT_MODEL = "gemini-3-pro-image-preview"
API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


def load_env():
    """Read KEY=VALUE pairs from .env at the repo root, then let real
    environment variables override them."""
    env = {}
    envfile = ROOT / ".env"
    if envfile.exists():
        for line in envfile.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    for key in ("GOOGLE_AI_API_KEY", "GOOGLE_AI_IMAGE_MODEL"):
        if os.environ.get(key):
            env[key] = os.environ[key]
    return env


def main():
    parser = argparse.ArgumentParser(
        description="Generate a brand-styled illustration via Gemini (Nano Banana Pro)."
    )
    parser.add_argument("--slug", required=True,
                        help="short identifier, used in the output filename")
    parser.add_argument("--prompt-file", required=True,
                        help="path to a text file containing the full prompt")
    parser.add_argument("--ref", nargs="*", default=[],
                        help="reference image paths (relative to the repo root)")
    parser.add_argument("--aspect", default="16:9",
                        help="aspect ratio, e.g. 16:9 (slides), 1:1, 9:16")
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("GOOGLE_AI_API_KEY", "")
    model = env.get("GOOGLE_AI_IMAGE_MODEL") or DEFAULT_MODEL

    if not api_key:
        sys.exit(
            "ERROR: GOOGLE_AI_API_KEY is not set.\n"
            "AI illustration generation is optional. To enable it:\n"
            "  1. Copy .env.example to .env\n"
            "  2. Add your Google AI Studio key: GOOGLE_AI_API_KEY=...\n"
            "     (get one at https://aistudio.google.com/apikey)\n"
            "Without a key, build decks from screenshots, icons and tokens instead."
        )

    prompt_path = pathlib.Path(args.prompt_file)
    if not prompt_path.exists():
        sys.exit(f"ERROR: prompt file not found: {prompt_path}")
    prompt = prompt_path.read_text()
    if not prompt.strip():
        sys.exit(f"ERROR: prompt file is empty: {prompt_path}")

    # Build the multimodal request: prompt text + optional reference images.
    parts = [{"text": prompt}]
    for ref in args.ref:
        ref_path = (ROOT / ref).resolve()
        if not ref_path.exists():
            sys.exit(f"ERROR: reference image not found: {ref_path}")
        mime = mimetypes.guess_type(str(ref_path))[0] or "image/png"
        parts.append({
            "inline_data": {
                "mime_type": mime,
                "data": base64.b64encode(ref_path.read_bytes()).decode(),
            }
        })

    url = f"{API_BASE}/{model}:generateContent"
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": args.aspect},
        },
    }

    try:
        response = requests.post(url, params={"key": api_key}, json=payload, timeout=180)
    except requests.RequestException as exc:
        sys.exit(f"ERROR: request to Gemini failed: {exc}")

    if response.status_code != 200:
        sys.exit(f"ERROR: Gemini API returned {response.status_code}: {response.text[:2000]}")

    data = response.json()
    img_b64 = None
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                img_b64 = inline["data"]
                break
        if img_b64:
            break

    if not img_b64:
        sys.exit(
            "ERROR: no image found in the Gemini response. "
            "The model may have refused the prompt or returned text only.\n"
            f"Raw response (truncated): {json.dumps(data)[:2000]}"
        )

    OUTDIR.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    png_path = OUTDIR / f"{today}-{args.slug}.png"
    png_path.write_bytes(base64.b64decode(img_b64))

    # JSON sidecar — journals exactly what was sent, for reproducibility.
    sidecar_path = OUTDIR / f"{today}-{args.slug}.json"
    sidecar_path.write_text(json.dumps({
        "slug": args.slug,
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "model": model,
        "aspect_ratio": args.aspect,
        "reference_images": args.ref,
        "prompt_file": str(args.prompt_file),
        "full_prompt_sent": prompt,
        "prompting_method": "Nano Banana Pro doctrine (see .claude/skills/generate-image.md)",
        "brand_source": "brand/guidelines.md + brand/tokens.css",
        "output": png_path.name,
    }, ensure_ascii=False, indent=2))

    print(f"OK -> {png_path}")
    print(f"     {sidecar_path}")


if __name__ == "__main__":
    main()
