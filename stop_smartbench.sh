#!/bin/bash

echo "Stopping all SmartBench processes..."

# Kill user-owned
pkill -f weather_influx.py
pkill -f button_control.py

# Kill root-owned (LED controller, raspotify)
sudo pkill -f led_weather.py
sudo pkill -f raspotify

# Remove pending notifications
rm -f /tmp/notify_leds

echo "All SmartBench processes stopped."
