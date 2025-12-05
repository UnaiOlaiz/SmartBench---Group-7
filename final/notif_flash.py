import time
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color

PIN = 18
NUM_LEDS = 10
strip = GroveWS2813RgbStrip(PIN, NUM_LEDS)

for i in range(NUM_LEDS):
    strip.setPixelColor(i, Color(255, 255, 255))
strip.show()
time.sleep(0.1)

for i in range(NUM_LEDS):
    strip.setPixelColor(i, Color(0, 0, 0))
strip.show()
