#!/bin/bash

PROJECT="/home/admin/SmartBench---Group-7"
FINAL="$PROJECT/final"
VENV="$PROJECT/env/bin/activate"

cd $PROJECT
source $VENV

echo "Killing old SmartBench processes..."
sudo pkill -f led_weather.py
pkill -f weather_influx.py
pkill -f button_control.py
pkill -f voice_control.py
rm -f /tmp/notify_leds

systemctl start raspotify

cd $FINAL

echo "Starting Weather → Influx..."
python weather_influx.py &

echo "Starting LED controller..."
sudo ../env/bin/python led_weather.py &

echo "Starting Button controller..."
python button_control.py &

echo "Starting Voice controller..."
sudo ../env/bin/python final/voice_control.py &

echo "SmartBench is now running in backgro
und (CLI mode)."
