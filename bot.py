import pyautogui as pag
from random import randint
from time import sleep

while True:
    x = randint(600,700)
    y = randint(600,700)
    pag.moveTo(x,y,0.5)
    sleep(2)