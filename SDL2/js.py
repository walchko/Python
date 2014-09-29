#!/usr/bin/env python
#
# by Kevin J. Walchko 26 Aug 2014
#
# PS4 has 6 axes, 14 buttons, 1 hat
# This program doesn't grab all buttons, just the most useful :)

import sdl2
import time

def prettyPrintPS4(ps4):
	print '------------------------------------'
	print '    press [SHARE] button to quit     '
	print '   left axis (x,y):',ps4['la']['x'],ps4['la']['y']
	print '  right axis (x,y):',ps4['ra']['x'],ps4['ra']['y']
	print '---'
	print '  left trigger1:',ps4['lt1'],'\t\t','right trigger1:',ps4['rt1']
	print '  left trigger2:',ps4['lt2'],'\t\t','right trigger2:',ps4['rt2']
	print '---'
	print '    square:',ps4['square']
	print '  triangle:',ps4['triangle']
	print '    circle:',ps4['circle']
	print '         x:',ps4['x']
	print '---'
	print '  hat:',ps4['hat']

# init stuff
sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

js = sdl2.SDL_JoystickOpen(0)

# grab info
a = sdl2.SDL_JoystickNumAxes(js)
b = sdl2.SDL_JoystickNumButtons(js)
h = sdl2.SDL_JoystickNumHats(js)
print 'axes:',a,'buttons:',b,'hats:',h

# Data structure holding the PS4 info
ps4 = {
	'la': {'x': 0, 'y': 0},  # left axis
	'ra': {'x': 0, 'y': 0},
	'lt1': 0, # left trigger 1
	'rt1': 0,
	'lt2': 0, # left trigger 2
	'rt2': 0,
	'circle': 0,  
	'triangle': 0,   
	'square': 0,
	'x': 0,
	'hat': 0,
	}

while True:
	sdl2.SDL_JoystickUpdate()
	
	# left axis
	ps4['la']['x'] = sdl2.SDL_JoystickGetAxis(js,0)
	ps4['la']['y'] = sdl2.SDL_JoystickGetAxis(js,1)
	
	# right axis
	ps4['ra']['x'] = sdl2.SDL_JoystickGetAxis(js,2)
	ps4['ra']['y'] = sdl2.SDL_JoystickGetAxis(js,5)
	
	# left trigger axis
	ps4['lt2'] = sdl2.SDL_JoystickGetAxis(js,3)
	
	# right trigger axis
	ps4['rt2'] = sdl2.SDL_JoystickGetAxis(js,4)
	
	# get buttons
	ps4['square'] = sdl2.SDL_JoystickGetButton(js,0)
	ps4['x'] = sdl2.SDL_JoystickGetButton(js,1)
	ps4['circle'] = sdl2.SDL_JoystickGetButton(js,2)
	ps4['triangle'] = sdl2.SDL_JoystickGetButton(js,3)
	ps4['lt1'] = sdl2.SDL_JoystickGetButton(js,4)
	ps4['rt1'] = sdl2.SDL_JoystickGetButton(js,5)
	
	# use share button as a quit
	quit = sdl2.SDL_JoystickGetButton(js,8)
	
	# get hat
	ps4['hat'] = sdl2.SDL_JoystickGetHat(js,0)
	
	prettyPrintPS4(ps4)
	
	if quit == True:
		break
	
	time.sleep(0.3)
 
sdl2.SDL_JoystickClose(js)
print 'Bye ...'

