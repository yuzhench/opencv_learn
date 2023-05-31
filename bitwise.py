import cv2 as cv
import numpy as np

blank = np.zeros([500,500],dtype="uint8")

#draw a rectangle
rectangle = cv.rectangle(blank.copy(),(50,50),(450,450),255,-1)
circle = cv.circle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2),250,255,-1)


cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

#1. bitwise and
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("and", bitwise_and)

#2. bitwise or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitwise_or)

#3. bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("xor",bitwise_xor)

#4. bitwise not 
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("not",bitwise_not)

cv.waitKey(0)