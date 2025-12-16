# SmartBench – IoT project

## Overview
SmartBench (FriendBench-Deusto) is an IoT-based interactive bench designed to encourage social interaction in university spaces. The bench reacts to user presence and environmental conditions using LED lighting and music, while collecting anonymous usage data for visualization.
This project is developed as the final assignment of the IoT course and builds upon the initial IoT Challenge proposal.

## Features
- Button-based interaction (presence simulation)
- Ambient light detection (day/night awareness)
- RGB LED feedback
- Bluetooth / Spotify audio playback
- Data upload to ThingSpeak
- Automatic startup on Raspberry Pi boot

## Hardware
- Raspberry Pi
- Button (GPIO)
- RGB LED bar
- Bluetooth speaker

## Software & Technologies
- Python 3
- Bash scripting
- ThingSpeak (HTTP API)
- Spotify control (Raspotify / external device)
- Linux (crontab / systemd)

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
1. The system starts automatically on boot.
2. Ambient light is checked to determine activation.
3. When the button is pressed:
4. LEDs turn on
5. Music starts playing
6. Event is sent to ThingSpeak
7. Usage data is visualized on ThingSpeak dashboards.

## Documentation
- Full documentation is available in the GitHub Wiki, including:
  - Architecture
  - File-by-file explanation
  - Deployment
  - Dashboards
  - Replication guide

## Team – Group 7
Matěj Zýka
Aitor
Unai

License

Academic project – University of Deusto
