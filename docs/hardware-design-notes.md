# ESP32-P4 Hardware Design Notes

## Before starting

ESP32-P4 is a high-performance MCU, but a successful design depends heavily on the supporting hardware.

Check:

- stable power rails
- correct decoupling
- crystal circuit
- flash and PSRAM connections when used
- boot/reset circuitry
- PCB stack-up and layout

## PCB

For high-speed ESP32-P4 designs, follow Espressif layout recommendations. A multi-layer PCB is strongly recommended.

## Motor control / real-time applications

For applications such as FOC motor control, do not select the MCU only by CPU frequency. Also evaluate:

- ADC timing
- PWM peripherals
- interrupt latency
- communication interfaces
- software ecosystem

## Always verify

Before ordering:

1. Confirm exact chip part number.
2. Confirm silicon revision.
3. Compare schematic with the latest Espressif reference design.
4. Review ERC/DRC and power-up behavior.
