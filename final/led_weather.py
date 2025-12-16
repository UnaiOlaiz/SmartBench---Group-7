import time
import datetime
import os
from influxdb_client import InfluxDBClient
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color

# --- SETTINGS ---
INFLUX_URL = "https://eu-central-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = "Q-rOMlcDU2vvsAePzlEwvC93vLDVkY5mC_4XOdufNf31ULvr1qwrTEUNmuQ6dcL5zV_xlAjJBN4xqXNVvD2m3A=="
INFLUX_ORG = "Deusto"
INFLUX_BUCKET = "weather"
PIN = 18
NUM_LEDS = 10
TEMP_THRESHOLD = 10

led_strip = GroveWS2813RgbStrip(PIN, NUM_LEDS)

def get_latest_temperature():
    try:
        # Use a very short timeout (2 seconds) so it doesn't freeze the script
        client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG, timeout=2000)
        query_api = client.query_api()
        query = f'from(bucket: "{INFLUX_BUCKET}") |> range(start: -1h) |> filter(fn: (r) => r["_field"] == "temperature") |> last()'
        tables = query_api.query(query)
        for table in tables:
            for record in table.records:
                return float(record.get_value())
    except Exception as e:
        print(f"Database sync error: {e}")
        return None
    return None

if __name__ == "__main__":
    print("SmartBench is running")
    
    while True:
        # CHECK VOICE FIRST (Priority 1)
        if os.path.exists("/tmp/leds_off_mode"):
            for i in range(NUM_LEDS): led_strip.setPixelColor(i, Color(0,0,0))
            led_strip.show()
            time.sleep(0.5)
            continue # Skip the rest and go back to start

        # CHECK BUTTON SECOND (Priority 2)
        if os.path.exists("/tmp/notify_leds"):
            print("Notification Triggered!")
            for _ in range(3):
                for i in range(NUM_LEDS): led_strip.setPixelColor(i, Color(255,255,255))
                led_strip.show()
                time.sleep(0.2)
                for i in range(NUM_LEDS): led_strip.setPixelColor(i, Color(0,0,0))
                led_strip.show()
                time.sleep(0.2)
            os.remove("/tmp/notify_leds")

	# --- WEATHER UPDATE ---
        temp = get_latest_temperature()
        #temp = 8 # Forced value for testing
        
        if temp is not None:
            print(f" Real-time Temperature: {temp}°C")
            if temp < TEMP_THRESHOLD:
                for i in range(NUM_LEDS): 
                    led_strip.setPixelColor(i, Color(0, 0, 255))
            else:
                for i in range(NUM_LEDS): 
                    led_strip.setPixelColor(i, Color(255, 0, 0))
            led_strip.show()
        time.sleep(1) # Refresh rate


