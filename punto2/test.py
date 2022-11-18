import smbus2
import bme280
import time

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)


while(1):
	data = bme280.sample(bus, address, calibration_params)

	print("Timestamp: ",data.timestamp, "\n")
	print("Temperatura: ", data.temperature, "\n" )
	print("Presion: ", data.pressure, "\n")
	print("Humedad: ", data.humidity, "\n")
	time.sleep(1)

