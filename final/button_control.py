import time
import requests
import subprocess
from grove.gpio import GPIO

THINGSPEAK_API_KEY = "BCMTU7TODBUUTP93"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
UPLOAD_INTERVAL = 1   # seconds

BUTTON_PORT = 5
button = GPIO(BUTTON_PORT, GPIO.IN)

def notificacion():
    subprocess.Popen(["sudo", "/home/admin/SmartBench---Group-7/env/bin/python", "notif_flash.py"])

def send_to_thingspeak(value):
    data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": value
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=data, timeout=5)
        print(f"ThingSpeak → {value} | Response: {response.text}")
    except Exception as e:
        print("ThingSpeak Error:", e)

if __name__ == "__main__":
    print("Button controller running...")

    sending = False  

    try:
        while True:
            raw = button.read()
            pressed = (raw == 1)

            if pressed and not sending:
                print("Button pressed → START actions")

                notificacion()

                subprocess.run(["sudo", "systemctl", "start", "raspotify"])

                sending = True

            if not pressed and sending:
                print("Button released → STOP sending")
                sending = False

            if sending:
                send_to_thingspeak(1)
            else:
                send_to_thingspeak(0)

            time.sleep(UPLOAD_INTERVAL)

    except KeyboardInterrupt:
        print("Button controller stopped.")
