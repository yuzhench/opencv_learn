import cv2 as cv 
import numpy as np

img = cv.imread('picture/p2')
cv.imshow("img",img)
# #1. convert the img from RGB to gray 
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)
# # cv.waitKey(0)

# #2. blur the image 
# blur = cv.blur(img,(10,10),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)
# # cv.waitKey(0)

#3. edge cascade
canny = cv.Canny(img,125,175)
# cv.imshow("canny",canny)
# cv.waitKey(0)

#4. dilation the image 
dilated = cv.dilate(img,(7,7),iterations=1)
# cv.imshow("dilated",dilated)
 

#5. eroded the image 
enroded = cv.erode(dilated,(7,7),iterations=1)
# cv.imshow("enroded",enroded)
# cv.waitKey(0)

#6. resize the image
def resize_img(img,height, width):
    dimention = (height, width)
    return cv.resize(img,dimention)
img_resize = resize_img(img,200,200)
cv.imshow("img_resize",img_resize)
# cv.waitKey(0)

#7. crop the image 
cropped = img[0:200,0:200]
cv.imshow("cropped",cropped)
cv.waitKey(0)
