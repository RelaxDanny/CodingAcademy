# pip install pyautogui
# pip install opencv-python
import cv2 as cv
import numpy as np
import pyautogui
import sys

cv.namedWindow("Dinosaur")
cv.moveWindow("Dinosaur", 0, 500)

x = 60
y = 375

img_piece = cv.imread('weapon.png', cv.IMREAD_COLOR)
h, w = img_piece.shape[:2]
top_left = 0
while True:
    pic = pyautogui.screenshot(region=(0, 0, 1920, 1000))
    img_frame = np.array(pic)
    img_frame = cv.cvtColor(img_frame, cv.COLOR_RGB2BGR)
    method = eval("cv.TM_CCOEFF")

    res = cv.matchTemplate(img_piece, img_frame, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(img_frame, top_left, bottom_right, (0, 255, 0), 2)
    print(max_val, top_left)
    # pyautogui.click(x=top_left[0], y=top_left[1])
    
    cv.imshow('Dinosaur', img_frame)
    # cv.imwrite('Logitech_sample.png', img_frame)
    if top_left[0] == x and top_left[1] == y:
        pyautogui.click(x=x, y=y)

    key = cv.waitKey(1)
    print(key)
    if key == 27:
        break

