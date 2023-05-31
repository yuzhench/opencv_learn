import cv2 as cv
import numpy as np 

# change the image from RGB to gray 
img = cv.imread("picture/p2")
gray_img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
 
 
# get the blur of the image 
blur = cv.GaussianBlur(gray_img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur", blur)
 

# find the canny of the image 
canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)

# find the binary version of the image 
ret, thresh = cv.threshold(gray_img,125,255,cv.THRESH_BINARY)
cv.imshow("threshold",thresh)

 

#find the contours of the image by using threshold
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"we find {len(contours)} in the image")
 
# show the image of the contours in a blank image (the contours is a list)
blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("the blank img is ", blank)

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("the contours is ", blank)
cv.waitKey(0)

print(f"we find {len(contours)} in the image")



# #find the contours of the image by using canny
# contours, hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f"we find {len(contours)} in the image")
