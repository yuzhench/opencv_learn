import cv2 as cv
import numpy as np

img = cv.imread("picture/p2")
cv.imshow("img",img)
blank = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("blank",blank)
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),img.shape[0]//4,55,-1)
cv.imshow("circle",circle)

img_img = cv.bitwise_and(img,img,mask=circle)
cv.imshow("doule",img_img)

cv.waitKey(0)