# ESP32-P4 ECAD and 3D Model Notes

## EasyEDA

Community EasyEDA libraries may provide:

- schematic symbol
- QFN104 footprint
- 3D model

These can be useful references when moving to another CAD system.

## Fusion 360 workflow

A STEP model can be imported into Fusion 360 as a 3D component reference.

However, a 3D model alone does not guarantee:

- correct pin mapping
- correct pad dimensions
- correct exposed pad definition
- correct schematic symbol

Always verify against the official package drawing.

## KiCad reference

Espressif's official KiCad library contains ESP32-P4 footprint data:

https://github.com/espressif/kicad-libraries

## Verification checklist

Before PCB fabrication check:

- package name
- chip ordering code
- QFN pad count
- exposed thermal pad
- pin 1 orientation
- pad dimensions
- revision-specific requirements
