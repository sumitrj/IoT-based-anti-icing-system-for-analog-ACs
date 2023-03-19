
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

