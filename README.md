# ESP32-P4 Design Resources

A practical, link-first resource hub for engineers designing custom hardware around the Espressif ESP32-P4.

This repository was created to help makers and engineers who can find scattered ESP32-P4 information but need one checked starting point for chip selection, hardware design, ECAD/MCAD work, and small-quantity sourcing.

## What is included

- direct links to official ESP32-P4 documents and reference designs;
- current chip-variant and silicon-revision notes;
- a hardware-design checklist based on Espressif's latest guidance;
- motor-control/FOC architecture reminders;
- official KiCad symbol and footprint references;
- a practical EasyEDA/STEP/Fusion 360 workflow;
- a script that downloads current official Espressif KiCad files;
- small-quantity purchasing and international-forwarding notes;
- clear third-party source and license boundaries.

## Start here

1. [Official documentation and reference designs](docs/official-resources.md)
2. [Chip selection and current variants](docs/chip-selection-and-variants.md)
3. [Chip revisions and errata](docs/chip-revisions-and-errata.md)
4. [Hardware design notes](docs/hardware-design-notes.md)
5. [ECAD and 3D-model notes](docs/ecad-and-3d-models.md)
6. [Fusion 360 workflow](docs/fusion-360-workflow.md)
7. [Purchasing and shipping notes](docs/purchasing-and-shipping.md)

## Current facts checked on 2026-07-28

- Current datasheet: **ESP32-P4 Series Datasheet, pre-release v0.7**.
- Current hardware guide: **ESP32-P4 Hardware Design Guidelines v1.9**.
- Current v3.x parts listed in the datasheet:
  - `ESP32-P4NRW16X` — 16 MB in-package PSRAM;
  - `ESP32-P4NRW32X` — 32 MB in-package PSRAM.
- Package: **QFN104, 10 × 10 mm**.
- Espressif recommends the **v3.0-or-later reference schematic for new designs**.
- Espressif recommends at least a **4-layer PCB**.
- ESP32-P4 does **not** include Wi-Fi or Bluetooth.
- The official Espressif KiCad library lists both the older EOL ESP32-P4 entry and the current ESP32-P4X family, and provides an ESP32-P4 symbol and footprint.
- The official KiCad 3D-model folder did not visibly contain an ESP32-P4 STEP file when checked, so community/EasyEDA 3D models may still be useful for mechanical work after verification.

## Official documentation index

https://documentation.espressif.com/en/documentList?s=ESP32-P4&eol=false

## Download official KiCad references

Run:

```bash
python tools/fetch_official_kicad.py
```

The script downloads the current official footprint, symbol library, and license directly from `espressif/kicad-libraries` and records SHA-256 hashes locally. The downloaded third-party files are intentionally not committed here.

## Important limitations

This repository is **not** a finished Fusion 360 component library and does not claim that a third-party community footprint is production-verified.

A symbol, footprint, or 3D model must still be checked against:

- the latest datasheet;
- the exact ordering code;
- the silicon revision;
- the current schematic checklist;
- the current errata;
- the intended PCB process.

A visually correct 3D model does not prove that pin mapping, copper pads, exposed-pad geometry, paste mask, or revision-specific circuitry is correct.

## Licensing

Original documentation in this repository is released under [CC BY 4.0](LICENSE).

Third-party files and links remain subject to their original licenses and terms. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Contributing

Corrections and verified additions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

This is an independent community resource and is not an official Espressif repository. No warranty is provided. Verify all design data before ordering PCBs, buying production quantities, or assembling hardware.
