Summary
This program is used to take screenshots using just one
keystroke which is ~ key on the top left hand side of the 
keyboard. When the program is in morion it listens to all the
keyboard activities and takes a screenshot whenever the 
~ key is pressed. If you want to terminate the program
press alt + x and the program will stop.

How to use
1.  Make sure to check if you have the following files
    1a. Python 3 Interpretor
    1b. pyinput
    1c. numpy
    1d. opencv-python
    1e. pyautogui

2.  If you don't have any of these you can download it from the
    following links/commands

    Open this in your preffered web browser
    Python 3: https://www.python.org/downloads/

    Type these commands in your terminal
    pynput: pip install pynput
    numpy: pip install numpy
    opencv-python: pip install opencv-python
    pyautogui: pip install pyautogui

3.  File structure
    main.py -       The main file responsible to take the screenshots
    functions.py -  The functions file
    logs.dat -      Screenshot data is sored here to avoid saving
                    files with the same names

4.  Usage
    The user must open the main.py folder to activate the program,
    nce the program is activated the user can press ` on the keyboard 
    to take a screenshot. Once the user feels to close the program
    alt+x can be pressed on the keyboard to shutdown the program

5.  Where the screenshots are saves?
    The screenshots are saved in the same directory as the program
