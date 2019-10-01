# IoT-based-anti-icing-system-for-analog-Air Conditioner Systems

## Requirement
Considering Economic conditions of most population in India, it is rare to observe an average person purchase 2 air-conditioners in a decade. 

As time passes the performance of ACs starts to deteriorate. One of the issues observed is the icing in fluid transmission pipes. This icing prevents the AC for cooling the room further and also results in significant energy loss. 

General user responds to this condition by manually switching off the air-conditioner and waiting for the ice to melt. Once this ice is melted, the AC starts to function normally.

## Proposed Solution

#### 1. System to Monitor Pipe and Room temperature in real time.
#### 2. Interfacing the switch of the AC with Relay which can be controlled by digital signals(5V/0V) of Microcontrollers.
#### 3. Temperature Feedback based system to switch off AC as pipe temperature gies below 5 degrees C.

## Hardware Requirements

##### 1. Atmel AT Tiny 85 - Microcontroller
##### 2. TTL based ADC
##### 3. Raspberry Pi 0
##### 4. A pair of LM-35 Temperature Sensors
##### 5. Relay module with impedence matching circuit

## Software Requirements
##### 1. Embedded C IDE for programming the AT Tiny 85
##### 2. Python 3.6
##### 3. SMTP - Library to send Emails
##### 4. Serial - Library to read values from microcontroller through USB port
##### 5. Firebase API for python

## Workflow:

### In Microcontroller (ATMEL ATTiny85):

    Temperature of the pipe and the room are aqcuired using a pair of LM35 and a DTH11
    
        if(pipe temperature is less than 5 degrees Celcius):
            Send Signal to Relay to switch off the AC
        else if(Room Temperature is less than 20 degrees Celcius and humidity is less than 20%):
             Send Signal to Relay to switch off the AC
        else 
          Send Signal to Relay to switch On the AC
       
### In Microcomputer (Raspberry Pi):

    Take the Temperature Values from the Microcontroller through Serial Port
    
    if(pipe temperature is less than 5 degrees Celcius):
        SendMail('Frozen')
    else
        SendMail(Room Environment Temperature)
  
### The reader is advised to visit https://console.firebase.google.com and create a new project in order to obtain API keys needed to open, store and access database on firebase
