#!/bin/bash

sudo modprobe w1-gpio
sudo modprobe w1_therm
file_path="/sys/bus/w1/devices/28-3c07f6490d2a/temperature"
while true
do	
	daten=$(date +%Y%m%d)
	temp=$(cat ${file_path})
	rem=$(($temp % 1000))
	int=$(($temp / 1000))
	n_temp="${int}.${rem}"
	time=$(date +%Y%m%d" "%H:%M:%S)
	out_line="${time},${n_temp}"
	echo $out_line  
	out_filename=${daten}_TEMPERATURA.csv
	echo  "${out_line}" >> $out_filename
	sleep 1
done
