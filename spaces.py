#transfer the image throught each color space 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgg = cv.imread("picture/p2")

cv.imshow("img",imgg)
print("hellow world")
cv.waitKey(0)


# img = plt.imread("picture/p2")
# plt.imshow(img)
# plt.show()
 

# #1. change the image from BGR to Gray 
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# #2. change the image from BGR to GRB
# img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

# #3. change the image from BGR to LAB
# img_lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)

# #4. chaneg the image from BGR to HSV
# img_HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# cv.imshow("gray image",gray)
# cv.waitKey(0)
