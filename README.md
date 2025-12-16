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
```bash
├── bluez-alsa
├── final
│   ├── button_control.py
│   ├── influxdata-archive_compat.key
│   ├── led_weather.py
│   ├── notif_flash.py
│   ├── weather_influx.py
│   └── voice_control.py
├── grove.py
├── old
│   ├── audio_manager.py
│   ├── button.log
│   ├── buttonThingSpeak.py.viejo
│   ├── cron.log
│   ├── led.log
│   ├── light_sensor.py
│   ├── lights.py
│   ├── lightsV2.py.viejo
│   ├── trial.txt
│   ├── wake_sony.sh
│   ├── weatherleds.py
│   └── weather.log
├── __pycache__
│   └── lightsV2.cpython-313.pyc
├── README.md
├── spotify-control.sh
├── start_cli.sh
└── stop_smartbench.sh
```

## Documentation
- Full documentation is available here <a href="https://github.com/UnaiOlaiz/SmartBench---Group-7/wiki">GithubWiki.


## Team – Group 7
- Matěj Zýka
- Aitor Goitia
- Unai Olaizola
