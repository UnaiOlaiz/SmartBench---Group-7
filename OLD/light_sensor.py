import time
from grove.grove_light_sensor_v1_2 import GroveLightSensor

TRESHOLD = 100

def main():
	sensor = GroveLightSensor(0)
	while True:
		light = sensor.light
		print(light)

		if light < TRESHOLD:
			print("DARK")
		else:
			print("LIGHT")
		time.sleep(1)

if __name__ == "__main__":
	main()
