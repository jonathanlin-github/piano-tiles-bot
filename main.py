from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver import ActionChains
#from selenium_move_cursor.MouseActions import move_to_element_chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get('http://tanksw.com/piano-tiles/')
time.sleep(2)
click(1055,371)



# y = 867
# tile 1 position: x: 806
# tile 2 position: x: 904
# tile 3 position: x: 988
# tile 4 position: x: 1082

# white = (255, 255, 255)
# black = (17,17,17)

start_time = time.time()
while keyboard.is_pressed('q') == False:
    
    time_elapsed = time.time() - start_time
    '''
    wait_time = None
    if time_elapsed <= 6:
        wait_time = 0.05
    if time_elapsed > 6:
        wait_time = .01
    wait_time = 0.00001
    #wait_time = 0.9 ** time_elapsed
    #wait_time = wait_time + .05
    #wait_time = wait_time * .1
    time.sleep(wait_time)
    '''
    if pyautogui.pixel(806, 800)[0] == 17:
        #actions = ActionChains(driver)
        #actions.send_keys('a')
        #actions.perform()
        if time_elapsed > 7:
            print('hi')
            click(806, 850)
        else:
            click(806, 800)
            print('bye')
    if pyautogui.pixel(904, 800)[0] == 17:
        if time_elapsed > 7:
            click(904, 850)
        else:
            click(904, 800)
    if pyautogui.pixel(988, 800)[0] == 17:
        if time_elapsed > 7:
            click(988, 850)
        else:
            click(988, 800)
    if pyautogui.pixel(1082, 800)[0] == 17:
        if time_elapsed > 7:
            click(1082, 850)
        else:
            click(1082, 800)
