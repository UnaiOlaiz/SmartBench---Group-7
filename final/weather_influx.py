import time
import requests
from influxdb_client import InfluxDBClient, Point, WriteOptions

API_KEY = "a43ccfe88d31b76d3d337f2572ed75fe"
CITY = "Bilbao"
COUNTRY_CODE = "ES"

INFLUX_URL = "https://eu-central-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = "Q-rOMlcDU2vvsAePzlEwvC93vLDVkY5mC_4XOdufNf31ULvr1qwrTEUNmuQ6dcL5zV_xlAjJBN4xqXNVvD2m3A=="
INFLUX_ORG = "Deusto"
INFLUX_BUCKET = "weather"

def get_temperature():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric"
    try:
        data = requests.get(url, timeout=5).json()
        if "main" in data:
            return data["main"]["temp"]
        return None
    except:
        return None

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

if __name__ == "__main__":
    while True:
        temp = get_temperature()
        if temp is not None:
            p = Point("bilbao_weather").field("temperature", temp)
            write_api.write(INFLUX_BUCKET, INFLUX_ORG, p)
            print(f"Stored temperature in {CITY}:, {temp}")
        else:
            print("Failed to get temperature.")
        time.sleep(60)
