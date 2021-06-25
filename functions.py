import numpy as np
import cv2
import pyautogui as pgui
import time
# imporing all the modules required

def Logs():
	# logs is used to keep track of all the info hapened in the last
	# taken screenshot
	# the code written above are used to remember the last screenshot

	# now this part makes a new input in the .dat file
	# firstly we use time
	scntime = time.strftime('%Y')+time.strftime('%m')+time.strftime('%d')+'-'+time.strftime('%H')+time.strftime('%M')+time.strftime('%S')+'-'+str(time.perf_counter_ns())
	write_scntime = 'Screenshot'+scntime
	
	# this return function spits out the last screenshot number
	return write_scntime

def Ts():
	nameread = Logs()
	final_name = nameread+'.png'
	image = pgui.screenshot()
	image = cv2.cvtColor(np.array(image),
	cv2.COLOR_RGB2BGR)

	cv2.imwrite(final_name, image)
