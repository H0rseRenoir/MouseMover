'''
MouseMover.py

Get starting mouse position
Wait randomly between 5-7 mins
If mouse hasn't moved, then move it to random location
If mouse has moved, do nothing

'''

import os
import logging
from time import sleep
from sys import exit
from random import randint, uniform

try:
	from pyautogui import size, moveTo, moveRel, position
except Exception:
	print('Error - missing pyautogui module - ' + str(Exception))
	print('Quitting')
	exit(1)

'''
Main block
'''
def main():
	configureLogging()
	moveMouse()

def configureLogging():
	global scriptName
	scriptName = os.path.splitext(os.path.basename(__file__))[0]
	
	logFile = os.path.join(os.getcwd(), scriptName) + '.log'
	
	if not os.path.isfile(logFile):
		logFile = open('myfile.dat', 'w+')
	
	print('logFile: ' + logFile)
	
	logging.basicConfig(
		filename	= logFile,	
		filemode	= 'a', 	
		format 		= '%(asctime)s %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
		datefmt		= '%Y-%m-%d %H:%M:%S',
		level		= logging.INFO
		)
	
	logging.info('Running ' + os.path.basename(__file__) + ' located in ' + os.getcwd())
	logging.info('logFile: ' + logFile)

def moveMouse():	
	#Get screen dimensions to move mouse randomly around the screen
	width, height = size()
	
	minSleepTime = 5 #minutes
	maxSleepTime = 7 #minutes

	count = 0
	
	while(True):
		savedPos = position() #cache mouse position
		
		print('found pos')
		sleepTime = uniform(minSleepTime * 60, maxSleepTime * 60) #sleep for random amount of time between min and max time
		logging.info('Determined current mouse position - sleeping for ' + str(sleepTime / 60) + ' minutes')
		sleep(sleepTime)
		
		if savedPos == position():
			print('moving mouse')
			logging.info("Mouse hasn't moved in " + str(sleepTime / 60) + ' mins - moving mouse')
			
			moveTo(randint(0, width), randint(0, height))
			
			count += 1
		else:
			print('not moving mouse')
			logging.info('Mouse has moved - not moving mouse')

if __name__ == '__main__':
	main()