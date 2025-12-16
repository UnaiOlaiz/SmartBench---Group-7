import time
import requests
from grove.gpio import GPIO
import subprocess
import os

THINGSPEAK_API_KEY = "BCMTU7TODBUUTP93"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
UPLOAD_INTERVAL = 15  # 15s interval to respect API limits

BUTTON_PORT = 5
button = GPIO(BUTTON_PORT, GPIO.IN)

def trigger_notification():
    open("/tmp/notify_leds", "w").close()

def send_to_thingspeak(value):
    data = {"api_key": THINGSPEAK_API_KEY, "field1": value}
    try:
        requests.post(THINGSPEAK_URL, data=data, timeout=2)
    except Exception as e:
        print("ThingSpeak Error:", e)

if __name__ == "__main__":
    print("Button controller running (Fast Response)...")
    sending = False
    last_upload = 0

    try:
        while True:
            pressed = (button.read() == 1)
            now = time.time()

            # 1. Instant Button Logic
            if pressed and not sending:
                print("Button pressed -> START actions")
                trigger_notification()
                subprocess.run(["sudo", "systemctl", "start", "raspotify"])
                sending = True
            
            if not pressed and sending:
                print("Button released -> STOP actions")
                subprocess.run(["sudo", "systemctl", "stop", "raspotify"])
                sending = False

            # 2. Upload Logic (Timer based, non-blocking)
            if now - last_upload > UPLOAD_INTERVAL:
                if sending: send_to_thingspeak(1)
                else: send_to_thingspeak(0)
                last_upload = now

            time.sleep(0.05) # Tiny sleep = Fast response

    except KeyboardInterrupt:
        print("Stopped.")
