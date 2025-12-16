import time
import requests
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color

API_KEY = "a43ccfe88d31b76d3d337f2572ed75fe"
CITY = "Bilbao"
COUNTRY_CODE = "ES"
TEMP_THRESHOLD = 8

PIN = 18
NUM_LEDS = 10
led_strip = GroveWS2813RgbStrip(PIN, NUM_LEDS)

def apagar_luces():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(0, 0, 0))
    led_strip.show()

def modo_frio():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(0, 50, 255))
    led_strip.show()

def modo_calor():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(255, 80, 0))
    led_strip.show()

def notificacion():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(255, 255, 255))
    led_strip.show()
    time.sleep(0.2)
    apagar_luces()

def get_temperature(city, country, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        print("DEBUG RESPONSE:", data)
        if "main" in data:
            return data["main"]["temp"]
        else:
            print("API error:", data.get("message"))
            return None
    except Exception as e:
        print("Error fetching temperature:", e)
        return None

if __name__ == "__main__":
    try:
        while True:
            notificacion()
            temp = get_temperature(CITY, COUNTRY_CODE, API_KEY)

            if temp is not None:
                print(f"Current Temperature in {CITY}: {temp}ºC")
                if temp < TEMP_THRESHOLD:
                    modo_frio()
                else:
                    modo_calor()
            else:
                apagar_luces()

            time.sleep(60)

    except KeyboardInterrupt:
        apagar_luces()
        print("Turning off the lights")
