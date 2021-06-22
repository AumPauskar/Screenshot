import  numpy as np
import cv2
import pyautogui as pgui
import time

def Logs():
    file = open('logs.dat', 'r')
    data = file.read()
    word = data.split('\n')
    
    last = word[1]

def Ts():
    image = pgui.screenshot()
    image = cv2.cvtColor(np.array(image),
    cv2.COLOR_RGB2BGR)

    cv2.imwrite(nameread, image)

Logs()