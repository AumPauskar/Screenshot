import  numpy as np
import cv2
import pyautogui as pgui
import time
# imporing all the modules required

def Logs():
    file = open('logs.dat', 'r')
    data = file.read()
    word = data.split('\n')
    last_num = int(word[1])
    last_num +=1
    last = 'screenshot'+str(last_num)
    file.close()
    # logs is used to keep track of all the info hapened in the last
    # taken screenshot
    # the code written above are used to remember the last screenshot

    # now this part makes a new input in the .dat file
    # firstly we use time
    curtime = time.strftime('%I')+':'+time.strftime('%M')+':'+time.strftime('%S')+' '+time.strftime('%p')+'\n'+time.strftime('%d')+'/'+time.strftime('%m')+'/'+time.strftime('%y')
    write_data = 'Screenshot\n'+str(last_num)+'\nLastScreenshot\n'+curtime
    file = open('logs.dat', 'w')
    file.write(write_data)
    file.close()
    
    # this return function spits out the last screenshot number
    return last

def Ts():
    nameread = Logs()
    final_name = nameread+'.png'
    image = pgui.screenshot()
    image = cv2.cvtColor(np.array(image),
    cv2.COLOR_RGB2BGR)

    cv2.imwrite(final_name, image)
    print(nameread)


Ts()