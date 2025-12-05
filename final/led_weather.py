import time
import datetime
import os
from influxdb_client import InfluxDBClient
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color

INFLUX_URL = "https://eu-central-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = "Q-rOMlcDU2vvsAePzlEwvC93vLDVkY5mC_4XOdufNf31ULvr1qwrTEUNmuQ6dcL5zV_xlAjJBN4xqXNVvD2m3A=="
INFLUX_ORG = "Deusto"
INFLUX_BUCKET = "weather"

PIN = 18
NUM_LEDS = 10
TEMP_THRESHOLD = 10

led_strip = GroveWS2813RgbStrip(PIN, NUM_LEDS)

def blue_mode():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(0, 0, 255))
    led_strip.show()

def red_mode():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(255, 0, 0))
    led_strip.show()

def modo_fiesta():
    colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
    for r, g, b in colors:
        for i in range(NUM_LEDS):
            led_strip.setPixelColor(i, Color(r, g, b))
        led_strip.show()
        time.sleep(0.25)

def notificacion():
    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(255, 255, 255))
    led_strip.show()
    time.sleep(0.2)

    for i in range(NUM_LEDS):
        led_strip.setPixelColor(i, Color(0, 0, 0))
    led_strip.show()

def get_latest_temperature():
    query_api = client.query_api()

    query = f'''
        from(bucket: "{INFLUX_BUCKET}")
          |> range(start: -1h)
          |> filter(fn: (r) => r["_measurement"] == "bilbao_weather")
          |> filter(fn: (r) => r["_field"] == "temperature")
          |> last()
    '''

    try:
        tables = query_api.query(query)
        for table in tables:
            for record in table.records:
                return float(record.get_value())
    except Exception as e:
        print("Error querying InfluxDB:", e)
        return None

    return None


client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)

if __name__ == "__main__":
    print("LED controller running...")

    while True:

        if os.path.exists("/tmp/notify_leds"):
            notificacion()
            os.remove("/tmp/notify_leds")

        day = datetime.datetime.today().weekday()
        if day in (4, 5):
            modo_fiesta()
            continue

        temp = get_latest_temperature()
        if temp is None:
            print("No temperature data found. Waiting...")
            time.sleep(5)
            continue

        print(f"Latest temperature: {temp}°C")

        if temp < TEMP_THRESHOLD:
            blue_mode()
        else:
            red_mode()

        time.sleep(2)
