# SmartBench – IoT project
This project is developed as the final assignment of the IoT course and builds upon the initial IoT Challenge proposal.

## Overview
Smartbench is the final project for our IoT subject for this course, for which we have created an intelligent bench with an integrated RaspberryPi to encourage social cohesion around university campuses and social areas using the latest 4.0 technology. Having a futuristic and appealing design, our bench will be reactive to human interaction through tools such as databases in the cloud, API interactions, and many more sensors and actuators.

## Features
- Button-based interaction
- RGB LED feedback
- Spotify music playback (not working now)
- Data upload to ThingSpeak

## Hardware
- Raspberry Pi + groove base hat
- Button (GPIO)
- RGB LED bar
- Speaker

## Software & Technologies
- Python 3
- Bash scripting
- ThingSpeak (HTTP API)
- Spotify control with Raspotify
- Linux 

## Repository Structure
├── audio_manager.py        # Audio & Spotify control
├── buttonThingSpeak.py     # Button logic + ThingSpeak upload
├── light_sensor.py         # Ambient light detection
├── lightsV2.py             # RGB LED control (final version)
├── weatherleds.py          # External weather-based LED logic
├── bluez-alsa/             # Bluetooth audio support
├── start_cli.sh            # System startup script
├── stop_smartbench.sh      # Safe shutdown script
├── spotify-control.sh      # Spotify playback control
├── wake_sony.sh            # Bluetooth speaker wake-up
└── README.md

## How It Works
1. 
2. Ambient light is checked to determine activation.
3. When the button is pressed:
4. LEDs turn on
5. Music starts playing
6. Event is sent to ThingSpeak
7. Usage data is visualized on ThingSpeak dashboards.

## Documentation
- Full documentation is available in the GitHub <a href="https://github.com/UnaiOlaiz/SmartBench---Group-7/wiki">Wiki.


## Team – Group 7
Matěj Zýka
Aitor
Unai

License

Academic project – University of Deusto
