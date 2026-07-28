# Third-Party Notices

This repository mainly contains original summaries and links. It does not bundle Espressif datasheets, reference-design archives, community EasyEDA libraries, or other third-party files unless their license clearly permits redistribution and attribution is preserved.

## Espressif documentation

Espressif documentation and reference designs remain subject to Espressif's own terms. This repository links to the official sources instead of republishing those files.

Official ESP32-P4 documentation index:

https://documentation.espressif.com/en/documentList?s=ESP32-P4&eol=false

## Espressif KiCad library

The official `espressif/kicad-libraries` repository provides symbols, footprints, and selected 3D models. Its package metadata identifies the library license as `CC-BY-SA-4.0`.

Source:

https://github.com/espressif/kicad-libraries

License:

https://github.com/espressif/kicad-libraries/blob/main/LICENSE.md

This repository does not currently copy those library files. The helper script in `tools/` downloads them directly from the official repository so the original source and license remain clear.

## EasyEDA community libraries

EasyEDA community components may be useful as references, but each component may have different authorship and redistribution conditions. No EasyEDA community file is included here at present.

Before redistributing a community symbol, footprint, or 3D model:

1. identify the original author and source page;
2. check whether redistribution is permitted;
3. preserve attribution and license information;
4. verify the design against the latest official ESP32-P4 datasheet.
