# ESP32-P4 Chip Selection and Variants

## Current production family

The current ESP32-P4 Series datasheet lists these v3.x parts:

| Ordering code | In-package PSRAM | Temperature range | Package |
|---|---:|---:|---|
| `ESP32-P4NRW16X` | 16 MB | -40 °C to 85 °C | QFN104, 10 × 10 mm |
| `ESP32-P4NRW32X` | 32 MB | -40 °C to 85 °C | QFN104, 10 × 10 mm |

Official datasheet:

https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_en.pdf

The older non-`X` ESP32-P4 entries are marked EOL in Espressif's current KiCad library. Start a new design with the exact currently orderable `X` part number and use the v3.x reference schematic.

## Important system-level fact

ESP32-P4 does **not** integrate Wi-Fi or Bluetooth. A product that needs wireless connectivity normally pairs it with a separate Espressif C-series or S-series companion chip, depending on the required radio and software architecture.

Do not select P4 only because it is the newest or fastest ESP32. It is most useful when the design benefits from features such as:

- dual-core 400 MHz high-performance RISC-V processing;
- in-package 16 MB or 32 MB PSRAM;
- MIPI CSI/DSI, image processing, H.264 and display/camera interfaces;
- high-speed USB;
- Ethernet MAC;
- rich DMA and high-performance peripheral support;
- many GPIOs and multiple real-time peripherals.

## For FOC and multi-axis motor control

P4 includes MCPWM and ADC controllers, but CPU speed alone does not determine whether it is the right motor-control MCU.

Evaluate:

- the number of PWM generators and synchronization resources needed;
- ADC sampling timing and trigger synchronization;
- current-sense amplifier topology and ADC input range;
- interrupt and DMA behavior;
- fault/brake response paths;
- required control-loop frequency;
- whether one MCU should control all axes or each axis should have a local controller;
- software maturity and available motor-control examples;
- power-stage layout, current return paths, thermal design, and EMC.

For an 18-axis controller, the gate drivers, current-sense paths, power distribution, fault containment, connector count, thermal design, and PCB area may dominate the architecture long before CPU performance becomes the limiting factor.

## Before buying parts

1. Record the exact ordering code.
2. Ask the seller which silicon revision will be supplied.
3. Confirm that the marking and packing information match the official datasheet.
4. Do not mix an old non-`X` symbol/reference schematic with a new `X` part without checking every revision-specific requirement.
5. Buy a small quantity first and verify chip marking, power-up, boot mode, and basic peripherals before committing to a production quantity.
