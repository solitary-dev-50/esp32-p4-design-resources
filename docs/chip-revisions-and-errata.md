# ESP32-P4 Chip Revisions and Errata

Do not begin a new ESP32-P4 board from an old screenshot, old reference schematic, or an unverified community library. Confirm the exact ordering code and silicon revision first.

## Current recommendation for new designs

Espressif's latest hardware design guidelines state that new designs should use the reference schematic for **chip revision v3.0 or later**.

Official schematic checklist:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/schematic-checklist-esp32p4.html

## Important differences called out by Espressif

The official checklist identifies several differences between revisions v1.0/v1.3 and v3.0 or later, including:

- pin 54 definition
- a 1 MΩ resistor associated with USB DP on early revisions
- two 499 kΩ resistors and one 22 pF capacitor in the external DCDC feedback circuit

For revision v3.0 and later, pin 54 is defined as `VDD_HP_1`. In revisions v1.0 and v1.3 it is defined as `NC`.

Do not copy these values from this summary into a production design. Use the latest official schematic checklist and the latest SoC errata as the source of truth.

## Documents to check

- ESP32-P4 Series SoC Errata
- ESP32-P4 Series Datasheet
- ESP32-P4 Hardware Design Guidelines
- ESP32-P4 chip variants / ordering information
- the exact reference design matching the intended chip revision

Official ESP32-P4 document index:

https://documentation.espressif.com/en/documentList?s=ESP32-P4&eol=false

Related documentation and reference designs:

https://documentation.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/related-documentation-and-resources.html

## Before ordering PCBs

1. Record the exact chip ordering code.
2. Confirm the silicon revision supplied by the distributor.
3. Compare the schematic against the reference schematic for that revision.
4. Re-check pin 54, DCDC feedback components, USB-related revision notes, and all power pins.
5. Review the latest errata again immediately before fabrication.

## Why this matters

A symbol or footprint can look correct while the surrounding schematic is wrong for the silicon revision. Revision checks are therefore separate from footprint checks.
