#!/bin/bash
# Keep Sony SRS-XB10 Bluetooth sink awake for Spotify Connect

SINK="bluez_output.00_42_79_0E_D0_A0.1"  # replace with your exact sink name
FILE="$HOME/silence.wav"

# Loop the silent WAV forever
while true; do
    pw-play --target "$SINK" "$FILE"
done
