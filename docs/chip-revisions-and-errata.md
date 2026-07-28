# ESP32-P4 Chip Revisions and Errata

Do not begin a new ESP32-P4 board from an old screenshot, old reference schematic, or unverified community library. Confirm the exact ordering code and silicon revision first.

Last checked: **2026-07-28**.

## Current recommendation for new designs

Espressif's current hardware design guidelines say that new designs should use the reference schematic for **chip revision v3.0 or later**.

Official schematic checklist:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/schematic-checklist-esp32p4.html

Current v3.x ordering codes listed in the datasheet:

- `ESP32-P4NRW16X`
- `ESP32-P4NRW32X`

The current Espressif KiCad-library README marks the older ESP32-P4 entry as EOL and lists ESP32-P4X separately. Do not assume that an older non-`X` library entry, schematic, or BOM is automatically correct for a new `X` design.

## Differences explicitly called out by Espressif

The hardware guide identifies differences between revisions v1.0/v1.3 and v3.0 or later, including:

- pin 54 definition;
- a 1 MΩ resistor associated with USB DP on early revisions;
- two 499 kΩ resistors and one 22 pF capacitor in the external DCDC feedback circuit;
- USB PHY and low-power behavior details;
- revision-specific reference schematics.

For revision v3.0 and later, pin 54 is defined as `VDD_HP_1`. In revisions v1.0 and v1.3 it is defined as `NC`.

Do not copy the values above directly into a production design. They are only a reminder of what must be checked in the current official guide.

## Official errata

Latest ESP32-P4 SoC errata:

https://docs.espressif.com/projects/esp-chip-errata/en/latest/esp32p4/index.html

The errata covers:

- chip-revision identification;
- affected revisions;
- known issues;
- workarounds;
- fixes and solution status;
- revision-specific summaries.

## Documents to check together

- ESP32-P4 Series Datasheet;
- ESP32-P4 Series SoC Errata;
- ESP32-P4 Hardware Design Guidelines;
- exact chip-variant and ordering information;
- reference design matching the intended revision;
- ESP-IDF release notes for revision support.

Official ESP32-P4 document index:

https://documentation.espressif.com/en/documentList?s=ESP32-P4&eol=false

## Before ordering PCBs

1. Record the complete ordering code in the schematic and BOM.
2. Confirm the silicon revision expected from the supplier.
3. Compare the schematic with the v3.0-or-later reference schematic.
4. Re-check pin 54, DCDC feedback, USB revision notes, power pins, flash/PSRAM voltages, reset timing and strapping pins.
5. Review the latest errata immediately before fabrication.
6. Record the document versions and access date in the project notes.
7. Re-check the first received chips before approving a larger build.

## Why this is separate from footprint verification

A footprint can be mechanically correct while the surrounding circuit is wrong for the silicon revision. A symbol can also have correct pad numbers while the design still uses an obsolete power or USB circuit.

Treat these as three independent checks:

1. package/land-pattern correctness;
2. symbol pin mapping;
3. revision-specific schematic correctness.
