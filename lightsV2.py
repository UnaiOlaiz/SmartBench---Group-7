import time
from  grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color

#config de los pines
pin = 18
num_leds = 10
led_strip = GroveWS2813RgbStrip(pin, num_leds)

#funciones
def apagar_luces():
	for i in range(num_leds):
		led_strip.setPixelColor(i, Color(0, 0, 0))
	led_strip.show()

def modo_tranquilo():
	#chill, just blue matej
        for i in range(num_leds):
                led_strip.setPixelColor(i, Color(0, 0, 50))
        led_strip.show()

def modo_fiesta():
	#fast colors
	colors = [
		(255, 0, 0),
		(0, 255, 0),
		(0, 0, 255),
		(255, 255, 0)
	]
	for r, g, b in colors:
		for i in range(num_leds):
			led_strip.setPixelColor(i, Color(r, g , b))
		led_strip.show()
		time.sleep(0.5)

def notificacion():
	#flash
	for i in range(num_leds):
		led_strip.setPixelColor(i, Color(255, 255, 255))
	led_strip.show()
	time.sleep(0.5)
	apagar_luces()

if __name__ == '__main__':
	try:
		while True:
			modo_fiesta()
	except KeyboardInterrupt:
		apagar_luces()
