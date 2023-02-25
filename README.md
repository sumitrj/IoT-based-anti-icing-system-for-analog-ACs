
IoT-based Anti-Icing System for Analog ACs
This repository contains the code and schematics for an Internet of Things (IoT)-based anti-icing system for analog air conditioners (ACs). The system is designed to prevent the build-up of ice on the evaporator coils of the AC, which can reduce the efficiency of the AC and potentially damage the compressor.

The system consists of a microcontroller (ESP8266) connected to a temperature and humidity sensor (DHT11), a relay module, and a heating element. The microcontroller reads the temperature and humidity data from the sensor and uses it to control the relay module, which turns the heating element on and off as needed to prevent the build-up of ice on the evaporator coils.

Getting Started
Prerequisites
To use this system, you'll need:

An analog AC unit with a working evaporator coil
A heating element (such as a resistive wire or PTC thermistor)
An ESP8266 microcontroller
A DHT11 temperature and humidity sensor
A relay module
You'll also need a basic understanding of electronics and programming in order to assemble the hardware and upload the code to the microcontroller.

Installing
To use the system, follow these steps:

Assemble the hardware according to the schematic provided in the repository (schematics/anti-icing-system-schematic.png).

Connect the ESP8266 to your computer and upload the code (src/anti_icing_system.ino) using the Arduino IDE or another suitable programming environment.

Connect the heating element to the relay module and the relay module to the microcontroller, following the pin assignments in the code.

Power on the system and monitor the temperature and humidity readings using the serial monitor in the Arduino IDE or a similar tool.

Adjust the temperature and humidity thresholds in the code as needed to suit your specific AC unit and environment.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the work of other DIY anti-icing system builders and is intended as a proof-of-concept for an IoT-based system. Special thanks to the creators of the DHT11 and ESP8266 libraries for making this project possible.
