# ESP32-P4 ECAD and 3D Model Notes

This page separates three things that are often confused:

1. schematic symbol;
2. PCB footprint/land pattern;
3. mechanical 3D model.

A useful file in one category does not automatically validate the other two.

Last checked: **2026-07-28**.

## Official Espressif KiCad resources

Repository:

https://github.com/espressif/kicad-libraries

The current official library provides an ESP32-P4 symbol and footprint. The README also distinguishes the older EOL ESP32-P4 entry from the current ESP32-P4X family.

### Official footprint

Browser view:

https://github.com/espressif/kicad-libraries/blob/main/footprints/Espressif.pretty/ESP32-P4.kicad_mod

Raw file:

https://raw.githubusercontent.com/espressif/kicad-libraries/main/footprints/Espressif.pretty/ESP32-P4.kicad_mod

### Official symbol library

https://github.com/espressif/kicad-libraries/blob/main/symbols/Espressif.kicad_sym

The symbol is stored inside the main Espressif symbol library rather than as a standalone file.

### License

The Espressif KiCad package metadata identifies the library as `CC-BY-SA-4.0`.

https://github.com/espressif/kicad-libraries/blob/main/LICENSE.md

Use `tools/fetch_official_kicad.py` in this repository to download the current files directly from Espressif and record local SHA-256 hashes.

## Official package facts

The current datasheet describes:

- package: QFN104;
- body: 10 × 10 mm;
- 104 perimeter pins plus the exposed pad;
- current v3.x variants: `ESP32-P4NRW16X` and `ESP32-P4NRW32X`.

Datasheet:

https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_en.pdf

Use the datasheet package drawing as the primary mechanical source and the official KiCad footprint as a second, implementation-level reference.

## EasyEDA community components

A community EasyEDA part may include:

- schematic symbol;
- QFN104 footprint;
- 3D model;
- supplier/order metadata.

That can save time, especially when Fusion 360 needs a STEP body, but do not treat the complete component as verified merely because all three previews appear.

Check separately:

- symbol pin names and numbers;
- footprint pad positions and dimensions;
- exposed-pad/paste geometry;
- pin-1 marker;
- exact chip ordering code and revision;
- 3D model dimensions and Z origin;
- original author and redistribution license.

No EasyEDA community file is included in this repository because the source page, author and redistribution permission have not yet been recorded.

## 3D model status

When checked, the official Espressif KiCad 3D-model folder did not visibly list an ESP32-P4 STEP model:

https://github.com/espressif/kicad-libraries/tree/main/3dmodels/espressif.3dshapes

Therefore, a verified EasyEDA/community STEP model can still be useful for:

- component-height checks;
- enclosure clearance;
- board renderings;
- collision checks in Fusion 360.

It should not be used to derive copper pads or pin mapping.

## Verification checklist

Before fabrication:

- [ ] Exact `ESP32-P4...X` ordering code selected.
- [ ] Silicon revision confirmed.
- [ ] Pin count and pin-1 location match the datasheet.
- [ ] Symbol pin table checked against the consolidated pin spreadsheet.
- [ ] QFN104 pad pitch and dimensions checked.
- [ ] Exposed pad and paste segmentation checked.
- [ ] Power, NC and reserved pins reviewed separately.
- [ ] Strapping pins identified.
- [ ] Footprint printed at 1:1 scale.
- [ ] 3D body aligned to the verified footprint, not the reverse.
- [ ] Third-party license and attribution recorded.

## What this repository can safely provide

- checked official links;
- workflow notes;
- downloadable official files through a helper script;
- verification checklists;
- independently created documentation under this repository's license.

## What should not be added without proof

- an EasyEDA export with unknown redistribution rights;
- a STEP file with no author/source;
- a Fusion device called "verified" without a pin-by-pin and pad-by-pad check;
- an old ESP32-P4 non-`X` symbol presented as current without revision notes.
