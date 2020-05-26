#!/usr/bin/env python3

import requests
import json
import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_url='http://dataservice.accuweather.com/currentconditions/v1/'
api_key = os.getenv('ACCUWEATHER_API_KEY')
location_key='298198'

response = requests.get(api_url + location_key + '?apikey=' + api_key)
data = json.loads(response.text)

current_temperature = data[0]['Temperature']['Metric']['Value']
conditions = data[0]['WeatherText']

print(' ' + str(current_temperature) + '°C' + ' ' + conditions)
