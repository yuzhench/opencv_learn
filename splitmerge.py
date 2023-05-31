import cv2 as cv
import numpy as np

img = cv.imread("picture/p2")
cv.imshow("img",img)

#1. print out the r g b 
b,g,r = cv.split(img)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

#2. merge r g b back to colorful img 
img_bgr = cv.merge([b,g,r])
cv.imshow("img_bgr",img_bgr)

#3. print the r g b with color 
# create a blank img and merge to a grb img
blank = np.zeros(img.shape[:2],dtype="uint8")
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

blue_green = cv.merge([b,g,blank])
cv.imshow("blue_green",blue_green)

bgr_img_bgr = cv.merge([blue,green,red])
# cv.imshow("bgr_img_bgr",bgr_img_bgr)
print(f"the shape of bgr_img_bgr is {bgr_img_bgr.shape}")

cv.waitKey(0)

 

