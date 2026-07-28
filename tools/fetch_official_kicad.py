#!/usr/bin/env python3
"""Download current official Espressif KiCad reference files.

The files are downloaded from the official espressif/kicad-libraries repository.
They are not vendored into this repository because they have their own license
and may change independently.
"""

from __future__ import annotations

import hashlib
import pathlib
import sys
import urllib.error
import urllib.request

BASE = "https://raw.githubusercontent.com/espressif/kicad-libraries/main"
FILES = {
    "ESP32-P4.kicad_mod": f"{BASE}/footprints/Espressif.pretty/ESP32-P4.kicad_mod",
    "Espressif.kicad_sym": f"{BASE}/symbols/Espressif.kicad_sym",
    "LICENSE.md": f"{BASE}/LICENSE.md",
}


def download(url: str, target: pathlib.Path) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "esp32-p4-design-resources/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    target.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    output_dir = pathlib.Path(__file__).resolve().parent.parent / "downloads" / "official-kicad"
    output_dir.mkdir(parents=True, exist_ok=True)

    source_lines = [
        "# Downloaded official Espressif KiCad files",
        "",
        "Source repository: https://github.com/espressif/kicad-libraries",
        "",
    ]

    for filename, url in FILES.items():
        target = output_dir / filename
        try:
            sha256 = download(url, target)
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"ERROR: could not download {url}: {exc}", file=sys.stderr)
            return 1
        print(f"Downloaded {filename}  sha256={sha256}")
        source_lines.extend(
            [
                f"## {filename}",
                "",
                f"- URL: {url}",
                f"- SHA-256: `{sha256}`",
                "",
            ]
        )

    (output_dir / "SOURCE.md").write_text("\n".join(source_lines), encoding="utf-8")
    print(f"Files written to: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
