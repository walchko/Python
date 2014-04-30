#!/usr/bin/env python

import  pywapi
import string

def printWeather(wr):
	print "==== " + wr['location']['name'] + " [" + wr['location']['lat'] + ',' + wr['location']['lon'] + "]==============="
	print "Current Temp: " + wr['current_conditions']['temperature'] + ' ' + wr['units']['temperature'] + ' ' + wr['current_conditions']['text']
	#print "Min/Max: " + 
	
	for i in wr['forecasts']:
		print i['day_of_week'] + ': \t' + i['low'] + ' ' + i['high'] + ' ' + i['day']['chance_precip'] + '% ' + i['day']['text']
	
def main():
	weather_com_result = pywapi.get_weather_from_weather_com('20105','')
	
	printWeather(weather_com_result)
	
	#yahoo_result = pywapi.get_weather_from_yahoo('20105')
	#noaa_result = pywapi.get_weather_from_noaa('KJFK')

	#print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + weather_com_result['units']['temperature'] + " now in " + weather_com_result['location']['name'] + ".\n\n"
	#print 
	
	#print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"

	#print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York.\n"
	
	#print str(weather_com_result) + "\n\n\n"
	
	#print str(yahoo_result) + '\n\n\n'
	
	#print str(noaa_result) + '\n\n\n'
	

if __name__ == '__main__':
    main()

