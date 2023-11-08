import requests
from win11toast import toast
import json
from scheduler import Scheduler
import time
import datetime as dt

schedule = Scheduler()


n = toast


#Api for the weather
URL = 'https://api.weather.gov/zones/forecast/NEZ002/forecast'



    #get the weather information
response = requests.get(URL)
forecast = response.json()['properties']
details = forecast['periods']
    

if details:
       
    period = details[0]
    nameInfo = period['name']
    details2 = period['detailedForecast']
    n(nameInfo + "\n", details2, icon='https://cdn1.iconfinder.com/data/icons/gardening-109/64/24_sunlight_sun_bright_sunshine_daylight_day_star_sun_rays-512.png', duration = 'long', button = 'Tonight')

    # Get the second period
def tonight():
    response = requests.get(URL)
    forecast = response.json()['properties']
    nightTime = forecast['periods']
    
    if nightTime:
    
        period1 = nightTime[1]
        nameInfo1 = period1['name']
        details3 = period1['detailedForecast']
        n(nameInfo1 + "\n", details3, duration = 'long')
    #button for the notification
buttons = [
    {'activationType': 'protocol', 'arguments':tonight(), 'content': 'Tonight'}]

    # Schedule the function to run every 2 hours
schedule.cyclic(dt.timedelta(hours=2))
schedule.cyclic(dt.timedelta(hours=2), tonight)

    # Keep the script running
while True:
    schedule.exec_jobs()
    time.sleep(1800)
        



    
    


    
    

     
    





