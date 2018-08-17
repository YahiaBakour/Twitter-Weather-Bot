
# coding: utf-8
''' TO USE THIS PROGRAM YOU NEED TO DOWNLOAD THE PYOWM AND TWEEPY PACKAGES: 
TO DOWNLOAD THEM FOLLOW THIS: open command prompt and run the following commands:
pip install tweepy
pip install pyowm
Creator : Yahia Bakour
Purpose : Pulls weather data from open weather module and posts tweets regarding weather conditions onto twitter on a set interval
 '''
 
'id={"name":"Yahia Bakour"'

import pyowm
import json
import tweepy
import time
from time import sleep #Used to delay the function before executing again

def tweetweather():
	numberofupdates = input("How many updates would you like to post today ?") #Asks the user for the number of updates
	frequency = input("How often would you like to post your updates (in seconds) ?") #Asks the user for the frequency of said updates
	for i in range(1,int(numberofupdates)): # loops the function to post every hour, allows for use of sleep function
        tweet_number = i # Tweet number is to prevent duplicate tweets which would yield an error, twitter does not allow duplicate tweets in a short period from a python function
		
        #MyOpenWeatherModule key
        owm = pyowm.OWM('417c9ccc727b5dd5a05b78afc2e2a605') 

        # Search for current weather in Boston
        observation = owm.weather_at_place('Boston,US')
        w = observation.get_weather()  
        # Weather details
        wind=w.get_wind()                  
        humidity=w.get_humidity()              
        temp=w.get_temperature('fahrenheit')
        tempc = w.get_temperature('celsius')
        status=w.get_status() 
		
        #Assigns variables to all of the current conditions I could choose to tweet
        windspeed = wind['speed'] #accesses wind dictionary to retrieve wind speeed
    

        #Converts temperature from a dict object into a float and finally into a string so it can be tweeted
        temperature= str(temp.get('temp')) #obtains temp in farenheiht and converts it into a string
        tempcelsius = str(tempc.get('temp')) #obtains temp in celsius

        #Actually accesses twitter using tweepy module, allows me to tweet out the weather
        CONSUMER_KEY = 'Enter Consumer Key Here'
        CONSUMER_SECRET = 'Enter Consumer Secret Key Here'
        ACCESS_KEY = 'Enter Access Key Here'
        ACCESS_SECRET = 'Enter Access_Secret Here'
		
		#Accesses twitter using tweepy and updates the status
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api =tweepy.API(auth)
		
		# Uses string formatting to update the status
        api.update_status('Update #{} : \nWeather conditions at BU : \nTemperature: {} F or {} C \nCondition: {} \nHumidity: {}% \nWind speed: {} m/s'.format(tweet_number,temperature,tempcelsius,str(status),str(humidity),str(windspeed)))
        time.sleep(int(frequency)) # Sleeps the function for the user inputted frequency.

		
tweetweather()




