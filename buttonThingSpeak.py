import time
import requests
from grove.gpio import GPIO

THINGSPEAK_API_KEY = "BCMTU7TODBUUTP93"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

BUTTON_PORT = 5
UPLOAD_INTERVAL = 1  # seconds

# Use Grove GPIO
button = GPIO(BUTTON_PORT, GPIO.IN)

def send_to_thingspeak(value):
    data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": value
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=data, timeout=5)
        print(f"Sent {value} | ThingSpeak response: {response.text}")
    except Exception as e:
        print("Error sending to ThingSpeak:", e)

if __name__ == "__main__":
    print("Sending continuous button state... Ctrl+C to exit.")

    try:
        while True:
            raw = button.read()
            pressed = 1 if raw == 1 else 0  

            print("Button state:", pressed)
            send_to_thingspeak(pressed)

            time.sleep(UPLOAD_INTERVAL)

    except KeyboardInterrupt:
        print("Stopped.")
