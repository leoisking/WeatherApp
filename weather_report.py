import requests
from win11toast import toast
import json

n = toast



URL = 'https://api.weather.gov/zones/forecast/NEZ002/forecast'





response = requests.get(URL)
forecast = response.json()['properties']



details = forecast['periods']

nightTime = forecast['periods']

if details:
    # Get the first period
    period = details[0]
    nameInfo = period['name']
    details2 = period['detailedForecast']
    n(nameInfo + "\n", details2, icon='https://cdn1.iconfinder.com/data/icons/gardening-109/64/24_sunlight_sun_bright_sunshine_daylight_day_star_sun_rays-512.png', duration = 'long', button = 'Tonight')

def tonight():
    if nightTime:
    # Get the first period
        period1 = nightTime[1]
        nameInfo1 = period1['name']
        details3 = period1['detailedForecast']
        n(nameInfo1 + "\n", details3, duration = 'long')

buttons = [
    {'activationType': 'protocol', 'arguments':tonight(), 'content': 'Tonight'}]


    
    


    
    

     
    





