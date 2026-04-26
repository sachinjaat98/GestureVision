import cv2 as cv
import numpy as np

def get_skin_mask(roi):
    hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    lower = np.array([2, 20, 70])
    upper = np.array([20, 255, 255])

    mask = cv.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.dilate(mask, kernel, iterations=2)
    mask = cv.erode(mask, kernel, iterations=1)
    mask = cv.GaussianBlur(mask, (3, 3), 0)

    return mask