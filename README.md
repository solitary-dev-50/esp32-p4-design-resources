# ESP32-P4 Design Resources

A practical, link-first resource hub for engineers designing custom hardware around the Espressif ESP32-P4.

This repository collects:

- official ESP32-P4 documentation and reference-design links
- a short hardware-design checklist
- chip-revision and errata reminders
- ECAD/MCAD resources that can help with symbols, footprints, and 3D models
- notes for moving between EasyEDA, KiCad, and Fusion 360

It does **not** replace the official datasheet, hardware design guidelines, errata, or reference designs. Always verify pin numbers, land patterns, power rails, strapping pins, and chip revision before fabrication.

## Start here

1. Read the [official resources list](docs/official-resources.md).
2. Check the [hardware design notes](docs/hardware-design-notes.md).
3. Confirm the exact chip and silicon revision using [chip revisions and errata](docs/chip-revisions-and-errata.md).
4. Use the [ECAD and 3D-model notes](docs/ecad-and-3d-models.md) when building or converting a library for your CAD tool.

## Important current notes

- For new designs, Espressif recommends using the reference schematic for **chip revision v3.0 or later**.
- ESP32-P4 is not a minimal-peripheral MCU. A basic design still needs the external power circuitry, crystal, flash, PSRAM where required, decoupling, boot/reset circuitry, and careful high-speed layout.
- Espressif recommends at least a **4-layer PCB** for ESP32-P4 designs.
- The official Espressif KiCad library already includes an ESP32-P4 symbol and footprint and can be used as a strong reference even when the final design is made in another CAD package.

## Documentation status

Checked on **2026-07-28**:

- ESP32-P4 Series Datasheet: v0.7
- ESP32-P4 Hardware Design Guidelines: v1.9

The official documents change over time. Prefer the `latest` pages linked in this repository rather than storing stale copies.

## Repository policy

- Official and third-party documents are linked rather than copied unless their license clearly permits redistribution.
- Community-created symbols, footprints, and 3D models must be checked against the latest Espressif documentation.
- A visually correct 3D model does not prove that the symbol, footprint, pin mapping, or exposed-pad geometry is correct.

## Main official index

Espressif ESP32-P4 document list:

https://documentation.espressif.com/en/documentList?s=ESP32-P4&eol=false

## Disclaimer

This is an independent community resource and is not an official Espressif repository. No warranty is provided. Verify all design data before ordering PCBs or assembling hardware.
