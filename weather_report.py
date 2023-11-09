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

    
#function to get the weather for the day
def get_weather():
    if details:
        period = details[0]
        nameInfo = period['name']
        details2 = period['detailedForecast']
        n(nameInfo + "\n", details2, duration = 'long', button = tonight ('Tonight'))

# function to get tonights weather
def tonight():
    if details:
        period1 = details[1]
        nameInfo1 = period1['name']
        details3 = period1['detailedForecast']
        n(nameInfo1 + "\n", details3, duration = 'long')
        
#button for the notification
buttons = [
    {'activationType': 'protocol', 'arguments':tonight(), 'content': 'Tonight'}]

# Schedule the function to run every 2 hours
schedule.cyclic(dt.timedelta(hours=2), get_weather)
schedule.cyclic(dt.timedelta(hours=2), tonight)

# Keep the script running
while True:
    schedule.exec_jobs(get_weather, tonight)
    time.sleep(1800)
        



    
    


    
    

     
    





