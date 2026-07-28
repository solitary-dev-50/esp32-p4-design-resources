# ESP32-P4 Official Resources

This page keeps the most useful official links in one place. Prefer these live official pages over copied files because Espressif updates the hardware guidance and errata over time.

Last checked: **2026-07-28**.

## Main document index

Espressif ESP32-P4 document list:

https://documentation.espressif.com/en/documentList?s=ESP32-P4&eol=false

## 1. ESP32-P4 Series Datasheet

Current checked version: **pre-release v0.7**.

PDF:

https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_en.pdf

Use it for:

- current ordering codes;
- QFN104 package drawing;
- pin names and pin numbers;
- power pins and operating limits;
- strapping/boot behavior;
- peripheral list;
- electrical characteristics;
- current chip-revision references.

Current v3.x variants listed in the datasheet:

- `ESP32-P4NRW16X`
- `ESP32-P4NRW32X`

## 2. Hardware Design Guidelines

Latest English guide:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/

Chinese guide:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/zh_CN/latest/esp32p4/

Current checked version: **v1.9**, dated 2026-07-21.

Revision history:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/revision-history.html

### Schematic checklist

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/schematic-checklist-esp32p4.html

Important current points:

- use the v3.0-or-later reference schematic for new designs;
- a basic P4 design still needs substantial external support circuitry;
- the minimum operating supply-current figure in the current guide includes flash and PSRAM;
- power, external DCDC, crystal, flash/PSRAM, reset, boot, USB and other interfaces all have revision-sensitive details.

### PCB layout guidance

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/pcb-layout-design-esp32p4.html

Espressif recommends at least a four-layer board for the high-speed design and interference-control requirements.

### Hardware/download guidance

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/hardware-development-esp32p4.html

## 3. SoC Errata

Latest ESP32-P4 errata landing page:

https://docs.espressif.com/projects/esp-chip-errata/en/latest/esp32p4/index.html

Use it to:

- identify chip revision;
- see which issues affect which revisions;
- check workarounds;
- confirm fixes before choosing parts or freezing a board revision.

## 4. Related documentation and reference designs

Official resource page:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/related-documentation-and-resources.html

It links to:

- Technical Reference Manual;
- consolidated pin-overview spreadsheet;
- chip variants;
- official KiCad library;
- development-board reference designs;
- product selector and technical support.

### Reference-design ZIP archives

ESP32-P4X Function EV Board:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/_downloads/3ccd3fcf4b943035f2313b42bcff07e7/ESP32-P4X-Function-EV-Board-EN.zip

ESP32-P4X EYE:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/_downloads/0857ce9b0e3668c3e56170a8a595db07/ESP32-P4X-EYE-EN.zip

Espressif notes that the `.DSN` files use OrCAD Capture 16.6 and the `.brd` files use Allegro 16.6. Check Espressif's reference-design terms before redistributing any of these files.

### Consolidated pin overview

https://documentation.espressif.com/ESP32-P4%20Appendix%20Consolidated%20Pin%20Overview.xlsx

This spreadsheet is useful for a manual pin-to-pad audit when building a CAD library.

## 5. Official KiCad library

Repository:

https://github.com/espressif/kicad-libraries

Official footprint:

https://github.com/espressif/kicad-libraries/blob/main/footprints/Espressif.pretty/ESP32-P4.kicad_mod

Raw footprint:

https://raw.githubusercontent.com/espressif/kicad-libraries/main/footprints/Espressif.pretty/ESP32-P4.kicad_mod

Symbol library:

https://github.com/espressif/kicad-libraries/blob/main/symbols/Espressif.kicad_sym

The official library currently lists the older ESP32-P4 entry as EOL and lists ESP32-P4X as the current family. The same package footprint may still be reused, but symbol names, pin definitions and revision-specific circuitry must be checked against the current datasheet.

## Recommended reading order

1. Current datasheet.
2. Chip variants and ordering code.
3. Current SoC errata.
4. Schematic checklist for the intended revision.
5. Reference design.
6. PCB layout chapter.
7. Technical Reference Manual for peripheral-level implementation.
8. Official KiCad data and CAD-tool conversion.

Before ordering PCBs, repeat steps 1 through 6 because these documents can change during the pre-release period.
