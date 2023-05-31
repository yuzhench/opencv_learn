import cv2 as cv
import numpy as np

img = cv.imread("picture/p2")
cv.imshow("img",img)

#1. average blur
average_blur = cv.blur(img,(3,3))
cv.imshow("average_blur",average_blur)

#2. guassian blur (less blur than average)
guassian_blur = cv.GaussianBlur(img,(3,3),0)
cv.imshow("guassian_blur",guassian_blur)

#3. median blur
median_blur = cv.medianBlur(img,3)
cv.imshow("median_blur",median_blur)

#4. bilateral blue 
bilateral_blur = cv.bilateralFilter(img,10,15,25)
cv.imshow("bilateral_blur",bilateral_blur)
cv.waitKey(0)
