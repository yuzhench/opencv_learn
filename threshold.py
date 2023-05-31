import cv2 as cv
import numpy as np

img = cv.imread("picture/p2")
cv.imshow("img",img)
grayed = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grayed",grayed)
#simple thresholding 
threshold_value, threshold = cv.threshold(grayed,155,255,cv.THRESH_BINARY)
cv.imshow("threshold",threshold)
#inverse thresholding 
threshold_value, threshold_inverse = cv.threshold(grayed,155,255,cv.THRESH_BINARY_INV)
cv.imshow("threshold_inverse", threshold_inverse)
cv.waitKey(0)

