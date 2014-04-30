#!/usr/bin/env python

import  pywapi
import string

# to help see better:
# for i in wr: print str(i) + ": " + str(wr[i]) + "\n\n"
# for i in wr['forecasts']: print str(i) + "\n\n" 

def printWeather(wr):
	c = wr['current_conditions']
	print "==== " + wr['location']['name'] + " [" + wr['location']['lat'] + ',' + wr['location']['lon'] + "]==============="
	print "Current Temp: " + c['temperature'] + ' ' + wr['units']['temperature'] + ' ' + c['text']
	print "Feels like: " + c['feels_like'] + ' ' + wr['units']['temperature'] 
	print 'Wind: ' + c['wind']['speed'] + ' ' + wr['units']['speed'] + ' ' + c['wind']['text'] 
	print 'UV index: ' + c['uv']['index'] + ' [' + c['uv']['text'] + ']'
	print c['moon_phase']['text'] + ' Moon'
	print '-------------------------------------------------'
	for i in wr['forecasts']:
		print i['day_of_week'] + ': \t' + i['low'] + ' ' + i['high'] + ' ' + i['day']['chance_precip'] + '% \t' + i['day']['text']
	
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

