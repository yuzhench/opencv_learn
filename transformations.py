import cv2 as cv
import numpy as np

img = cv.imread('picture/p2')
cv.imshow("img",img)

#1. image translation 
def translation (img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimention = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimention)
translated_img = translation(img,100,100)
cv.imshow("translated_img",translated_img) 
# cv.waitKey(0)

#2. rotate the image 
def rotation (img, angle, rot_point = None):
    width = img.shape[1]
    height = img.shape[0]
    dimention = (width, height)
    if rot_point == None:
        rot_point = (width//2,height//2)
    rot_matrix = cv.getRotationMatrix2D(rot_point,angle,1.0)
    return cv.warpAffine(img,rot_matrix,dimention), rot_matrix
rotation_img, r_mat = rotation(img,45)
cv.imshow("rotation_img",rotation_img)
# cv.waitKey(0)
# print(f"the rotation matrix is {r_mat}")

#3. resize the image 
resized = cv.resize(img,(600,600),interpolation=cv.INTER_AREA)
cv.imshow("resized",resized)
# cv.waitKey(0)

#4. flip the image 
flipped = cv.flip(img,0)
cv.imshow("flipped", flipped)
# cv.waitKey(0)

#5. cropping the image 
cropped = img[200:300,200:300]
cv.imshow("cropped",cropped)
cv.waitKey(0)


