#!/usr/bin/env python3
from psutil import sensors_temperatures

def format_output(temperature):
    return " " + temperature + "°C"

current_cpu_temp = sensors_temperatures()['k10temp'][0].current

print(format_output(str(current_cpu_temp)))
