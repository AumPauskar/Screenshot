import functions
from pynput import keyboard

def ActivateScreenshot():
    functions.Ts()

def ProgramClose():
    quit()

with keyboard.GlobalHotKeys({
    '`':ActivateScreenshot,
    '<alt>+x':ProgramClose}) as key:
    key.join()