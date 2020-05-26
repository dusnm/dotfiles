#!/usr/bin/env python3
#
# Copyright (C) 2020 Dusan Mitrovic <dusan@dusanmitrovic.xyz>
# Licensed under the terms of the GNU GPL v3 only
#
# i3blocks script to get the temperature of the CPU
from psutil import sensors_temperatures

def format_output(temperature):
    return " " + temperature + "°C"

current_cpu_temp = sensors_temperatures()['k10temp'][0].current

print(format_output(str(current_cpu_temp)))
