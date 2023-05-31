import cv2 as cv
import numpy as np


# fill an area in the blank
# blank = np.zeros((500,500,3),dtype='uint8')
# blank[10:200, 300:400] = 0,0,255
# cv.imshow("blank",blank)
# cv.waitKey(0)

# draw a rectangle in the blank picture
blank = np.zeros((500,200,3),dtype = 'uint8')
cv.rectangle(blank,(10,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=cv.FILLED)
# cv.imshow("the img",img)
# cv.waitKey(0)

# draw a circle 
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=2)
# cv.imshow("circle",blank)
# cv.waitKey(0)

#draw a line 
cv.line(blank, (0,0),(blank.shape[1],blank.shape[0]),(0,255,0),thickness=2)
# cv.imshow("line",blank)
# cv.waitKey(0)

#how to add text on the image
cv.putText(blank,"yuzhen chen ",(0,20),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),thickness=1)
cv.imshow("text",blank)


cv.waitKey(0)