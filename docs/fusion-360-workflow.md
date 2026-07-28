# Using ESP32-P4 Design Data in Fusion 360 Electronics

This repository does not provide a finished Fusion 360 library. The goal is to reduce the work and make the remaining work verifiable.

## What can be reused

From the official Espressif KiCad library:

- ESP32-P4 schematic symbol data;
- ESP32-P4 QFN104 footprint data;
- source and license information.

From a verified STEP model:

- package body size;
- board-level mechanical clearance;
- enclosure and heatsink checks;
- visual placement in Fusion 360.

A STEP model does not contain the schematic symbol, electrical pin mapping, or copper land pattern.

## Recommended workflow

### 1. Confirm the exact chip

Use the current `ESP32-P4NRW16X` or `ESP32-P4NRW32X` datasheet and confirm the silicon revision before creating the device.

### 2. Create or import the schematic symbol

Use the official Espressif KiCad symbol as a pin-name and grouping reference. In Fusion 360 Electronics, create the symbol and verify every pin number and name against the current datasheet.

Useful official source:

https://github.com/espressif/kicad-libraries/tree/main/symbols

### 3. Create the QFN104 package

Use both:

- the official package drawing in the ESP32-P4 datasheet;
- the official Espressif KiCad footprint as an implementation reference.

Official footprint:

https://github.com/espressif/kicad-libraries/blob/main/footprints/Espressif.pretty/ESP32-P4.kicad_mod

Raw footprint:

https://raw.githubusercontent.com/espressif/kicad-libraries/main/footprints/Espressif.pretty/ESP32-P4.kicad_mod

Check at least:

- 10 × 10 mm body;
- QFN104 pin count;
- pad pitch and pad dimensions;
- exposed-pad geometry;
- paste-mask segmentation;
- solder-mask expansion;
- pin-1 orientation;
- courtyard and assembly clearance.

### 4. Add the 3D package

Fusion 360 can import a STEP file into a 3D package. Align it using:

- package center;
- board surface/Z height;
- pin-1 marker;
- body rotation.

The current official Espressif KiCad 3D-model folder does not visibly include an ESP32-P4 STEP model, so a verified community/EasyEDA model may be useful for mechanical visualization. Treat it as a mechanical reference only until its source and dimensions have been checked.

### 5. Build the device mapping

Map every schematic pin to the correct package pad. The exposed pad is normally represented as its own pad number in the source library; verify how Fusion expects it to be connected and how the datasheet defines it.

### 6. Run a manual cross-check

Before using the device in a board:

1. export a pin-to-pad table;
2. compare it with the datasheet pin table;
3. check all power pins separately;
4. check NC/reserved pins separately;
5. check strapping and boot pins;
6. print the footprint at 1:1 scale;
7. run DRC and inspect paste openings.

## EasyEDA-to-Fusion notes

If a community EasyEDA component includes a 3D model:

1. place only that component on a temporary PCB;
2. open the 3D view and confirm the model is present;
3. export a STEP model if the EasyEDA edition supports it;
4. import the STEP into Fusion 360;
5. align it to the independently verified Fusion footprint.

Do not assume that an EasyEDA component's symbol, footprint, and 3D model were all created by the same author or verified against the same chip revision.
