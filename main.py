import pyautogui as pg
from random import randint
# mouse control function


# for i in range(5): 
pg.hotkey('win', 'm')
pg.hotkey('win', 'r')
pg.write("notepad") 
pg.press('enter')
pg.write("hello world") 


    # height = randint(0, 1080) 
    # weight = randint(0, 1920)
    # pg.click(weight, height)


    # pg.write("hello world", interval=0.25)


    # pg.hotkey('win', 'm')
    # pg.hotkey('fn', 'alt', 'f4')
    # pg.hotkey('left')
    # pg.hotkey('enter') # to put to sleep mode


    # pg.click(30, 1060, duration=1)  
    # pg.dragTo(100, 200, button='left') 

# pg.alert(text='hello', title='hello win', button='OK')