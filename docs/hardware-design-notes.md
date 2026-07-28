# ESP32-P4 Hardware Design Notes

This is a compact engineering checklist, not a replacement for Espressif's current hardware design guide.

Official guide:

https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32p4/

Last checked: **2026-07-28**.

## 1. The chip is not a minimal-support MCU

Espressif's current schematic checklist says the integrated circuitry still needs roughly 40 external resistors, capacitors and inductors, plus:

- a mandatory 40 MHz crystal;
- SPI flash;
- an external DCDC;
- power-entry and local decoupling;
- reset/boot circuitry;
- optional interfaces and protection components.

Plan the support circuitry and PCB area before choosing P4 only for CPU performance.

## 2. Power tree

The current guide recommends 3.3 V for a single external supply and states a minimum operating supply current of 380 mA including flash and PSRAM, before adding the current needed by external peripherals.

Check every rail individually:

- main 3.3 V input;
- VDD_HP groups;
- VDD_LP and IO rails;
- VDD_FLASHIO;
- 1.8 V PSRAM IO supply;
- VDD_ANA and VDD_BAT;
- USB PHY supply when used;
- MIPI PHY supplies when used;
- external DCDC input, output and feedback loop.

Do not estimate the board supply only from average CPU current. Include startup, memory, display/camera, USB, Ethernet, motor-control isolation, gate-driver and communication loads.

## 3. External DCDC

Use the current v3.x reference schematic and one of the DCDC parts currently verified by Espressif, or independently validate an alternative.

The guide currently lists:

- ETA3485;
- SY8088;
- RY3420;
- BL8028;
- LP3219;
- TLV62569.

Place the DCDC and feedback network close to the ESP32-P4. Keep the switching-current and feedback loops short and follow the exact revision-specific circuit.

## 4. Clock

The firmware currently supports a 40 MHz external crystal. Espressif specifies crystal accuracy within ±10 ppm in the hardware guide.

Treat crystal placement, ground isolation, load capacitors and trace symmetry as layout-critical.

## 5. Flash and PSRAM

Confirm:

- selected flash voltage;
- VDDO_FLASH configuration;
- flash CS pull-up;
- local decoupling;
- optional series-resistor footprints on high-speed SPI lines;
- in-package PSRAM variant and its 1.8 V IO supply;
- revision-specific pin mapping.

The `NRW16X` and `NRW32X` variants include 16 MB and 32 MB PSRAM respectively, but external flash is still required.

## 6. Reset, boot and download

Check:

- CHIP_PU timing;
- the current recommended RC values;
- boot-strapping pins;
- GPIO35 boot-mode behavior;
- UART0 download path;
- USB download path if used;
- ROM log access for bring-up.

Do not reuse reset values from an older P4 guide without checking the current revision history.

## 7. PCB stack-up and layout

Espressif recommends at least a four-layer PCB:

1. top — components and signals;
2. layer 2 — uninterrupted GND plane;
3. layer 3 — power and selected high-speed signals with a reference plane;
4. bottom — remaining signals.

Key layout priorities:

- keep the GND reference continuous;
- route main power with the widths recommended in the current guide;
- place decoupling at each power pin;
- keep the DCDC loop compact;
- isolate crystal routing;
- control USB and MIPI differential impedance where used;
- maintain return paths across layer changes;
- keep noisy power-stage currents away from ADC and clock regions.

## 8. Wireless connectivity

ESP32-P4 has no integrated Wi-Fi or Bluetooth. A connected product needs a separate wireless companion or a wired interface.

For a compact motor controller, decide early whether wireless communication belongs:

- on the same board through a companion ESP32-C/S device;
- on a separate communication board;
- or outside the real-time control system entirely.

## 9. FOC and multi-axis motor control

P4 has MCPWM, ADC controllers, DMA and a high-performance dual-core CPU, but an 18-axis FOC system should not be judged by clock speed alone.

### Control resources

Count before committing:

- complementary PWM outputs;
- dead-time generators;
- ADC channels and simultaneous/synchronized sampling needs;
- current-sense channels;
- fault/brake inputs;
- encoder/Hall/SPI interfaces;
- timer and DMA resources;
- control-loop and communication deadlines.

### Architecture choices

Compare at least these architectures:

1. one P4 controls all axes;
2. one local motor-control MCU per small group of axes, with P4 as supervisor;
3. one controller per axis, connected over CAN/TWAI, SPI or another deterministic bus.

A distributed design may be larger in component count but can simplify fault containment, routing, ADC timing, thermal management and software verification.

### Analog and power-stage reality

For 15 A-class axes, the critical design work includes:

- shunt value and dissipation;
- current-sense amplifier common-mode range and offset;
- ADC full-scale use and noise;
- gate-driver current and protection;
- MOSFET conduction/switching loss;
- DC-bus distribution;
- copper thickness and thermal paths;
- fault shutdown independent of firmware;
- EMI from eighteen switching bridges.

The MCU is only one part of the system.

## 10. Bring-up plan

Before assembling the full board:

1. verify all rails without the chip where practical;
2. assemble one minimal P4 section;
3. confirm reset, crystal and boot logs;
4. test external flash and PSRAM;
5. test one PWM/ADC control channel;
6. validate current-sense offset and gain over temperature;
7. verify hardware fault shutdown;
8. scale to more axes only after one channel is stable.

## Final pre-fabrication check

- [ ] Exact ordering code recorded.
- [ ] Silicon revision confirmed.
- [ ] Latest datasheet and errata reviewed.
- [ ] v3.x reference schematic used.
- [ ] Power-budget margin documented.
- [ ] DCDC and memory circuits checked.
- [ ] 40 MHz crystal circuit checked.
- [ ] Boot/reset/download path checked.
- [ ] Four-layer-or-better stack-up reviewed.
- [ ] Footprint, symbol and exposed pad checked independently.
- [ ] ADC/PWM/fault resources counted for the real application.
