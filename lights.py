import time
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color

# Use a PWM-capable pin (GPIO 18 works on most Raspberry Pis)
PIN = 18
NUM_LEDS = 10  # Change to however many LEDs you actually have

led_strip = GroveWS2813RgbStrip(PIN, NUM_LEDS)

def cycle_colors():
    colors = [
        (255, 0, 0),   # Red
        (0, 255, 0),   # Green
        (0, 0, 255),   # Blue
        (255, 255, 0), # Yellow
        (0, 255, 255), # Cyan
        (255, 0, 255), # Magenta
        (255, 255, 255), # White
        (0, 0, 0)      # Off
    ]
    for r, g, b in colors:
        led_strip.setPixelColor(0, Color(r, g, b))  # Use packed color
        led_strip.show()
        time.sleep(1)

try:
    while True:
        cycle_colors()
except KeyboardInterrupt:
    led_strip.setPixelColor(0, Color(0, 0, 0))
    led_strip.show()
