# this code automatically write a code to calculate squre root of user defined number
import pyautogui as pg
import time as t

pg.leftClick(174,94)
t.sleep(1)
pg.typewrite("squre.py")
t.sleep(1)
pg.press("enter")
t.sleep(1)
pg.typewrite("a = input('Enter number: ')")
t.sleep(1)
pg.press("enter")
t.sleep(1)
pg.typewrite("b = int(a) * int(a)")
t.sleep(1)
pg.press("enter")
t.sleep(1)
pg.typewrite("print('The squre of {0} is {1}'.format(a, b))")
t.sleep(1)
pg.press("enter")
t.sleep(1)
pg.hotkey("ctrl","s")
t.sleep(1)
pg.hotkey("ctrl","alt","n")
t.sleep(1)
pg.leftClick(1286,844)
t.sleep(1)


# t.sleep(3)
# print(pg.position())