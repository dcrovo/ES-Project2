import time
import smbus2
import bme280
import threading

# Se instancian objetos del sensor y librerias
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

file_1w_path='/sys/bus/w1/devices/28-3c07f6490d2a/temperature'
min_period=0.01

## Function to read 1-wire sensor temperature
def read_1w_temperature():
	while True:
		with open(file_1w_path, 'r', encoding='utf-8') as temperature_file:
			temp_raw = temperature_file.readline()
			temperature = float(temp_raw)/1000
			print('1w temperature: ',temperature)
			time.sleep(1)
		
def read_i2c_vars():
	while True:
		data = bme280.sample(bus, address, calibration_params)
		#return data.temperature, data.pressure, data.humidity
		print('i2c temperature:', data.temperature)
		print('i2c pressure: ', data.pressure)
		print('i2c humidity: ', data.humidity)
		
		time.sleep(min_period*100)
		
	
th_i2c_readout = threading.Thread(target=read_i2c_vars)
th_1w_readout = threading.Thread(target=read_1w_temperature)
def main():
	th_i2c_readout.start()
	th_1w_readout.start()

main()
