import numpy as np
from PIL import ImageGrab, Image
import cv2
# from directKeys import click, queryMousePosition
import pyautogui as clicker
from ctypes import windll, Structure, c_long, byref
import time

# these are Code Bullets coords
game_coords = [653, 585, 1142, 763]
# my screen is smaller these were my cordinates
# game_coords = [164, 608, 662, 726]


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))

    return pt.x, pt.y


def click_targeted_point(screen):
    global game_coords

    for y in range(5, len(screen) - 5):
        for x in range(5, len(screen[y]) - 5):
            if screen[y][x] < 10:
                actual_x = x + game_coords[0]
                actual_y = y + game_coords[1]
                # click(actual_x, actual_y)
                clicker.click(actual_x, actual_y)
                return


while True:
    mouse_posx, mouse_posy = queryMousePosition()
    if mouse_posx > 0:
        break

while True:
    mouse_posx, mouse_posy = queryMousePosition()

    if game_coords[0] < mouse_posx < game_coords[2] and game_coords[1] < mouse_posy < game_coords[3]:
        start_time = time.time()
        screen = np.array(ImageGrab.grab(bbox=game_coords))
        # print(screen)
        # image = Image.open(screen)
        # image.show()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        click_targeted_point(screen)
        print("Frame took (%s) seconds" % (time.time() - start_time))
