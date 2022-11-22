import time
import smbus2
import bme280

# Se instancian objetos del sensor y librerias
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

file_1w_path='/sys/bus/w1/devices/28-3c07f6490d2a/temperature'

	

## Function to read 1-wire sensor temperature
def read_1w_temperature():
	with open(file_1w_path, 'r', encoding='utf-8') as temperature_file:
		temp_raw = temperature_file.readline()
		temperature = float(temp_raw)/1000
	return temperature
		
def read_i2c_vars():
	data = bme280.sample(bus, address, calibration_params)

	return data.temperature, data.pressure, data.humidity
	
	
while True:
	t = read_1w_temperature();
	ti2c, p, h = read_i2c_vars()
	print(t)
	print(ti2c)
	print(p)
	print(h)
	time.sleep(1)
