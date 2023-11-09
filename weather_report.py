import requests
from win11toast import toast
import json
from scheduler import Scheduler
import time
import datetime as dt




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
        n(nameInfo + "\n", details2, duration = 'long', button = 'Tonight')

# function to get tonights weather
def tonight():
    if details:
        period1 = details[1]
        nameInfo1 = period1['name']
        details3 = period1['detailedForecast']
        n(nameInfo1 + "\n", details3, duration = 'long', button = 'Close')
        

  
  
get_weather()      
#button for the notification
buttons = [
    {'activationType': 'protocol', 'arguments':tonight(), 'content': 'Tonight'}]

buttons1 = [
    {'activationType': 'protocol', 'arguments' 'content': 'Close'}]

schedule = Scheduler()

# Schedule the function to run every 2 hours
schedule.hourly(dt.time(minute=30, second=15), get_weather)
schedule.hourly(dt.time(minute=30, second=15), tonight)

# Keep the script running
while True:
    schedule.exec_jobs()
    schedule.exec_jobs()
    time.sleep(1)
    

        



    
    


    
    

     
    




