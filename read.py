# import cv2 as cv
# # img = cv.imread('picture/p1')
# # # cv.imshow('picture',img)


# #resize function 
# def resize_fun(frame, scale = 0.75):
#     height = int(frame.shape[0]*scale)
#     width = int(frame.shape[1]*scale)
#     dimentions = (width,height)
#     return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture(4)

# # while True:
# #     isTrue, frame = capture.read()
# #     resize_frame = resize_fun(frame)
# #     cv.imshow('resize_video',resize_frame)
# #     cv.imshow('video',frame)
# #     if cv.waitKey(20) & 0xFF ==ord('d'):
# #         break
  

# # def resize_img_fun(frame, scale = 0.5):
# #     height = int(frame.shape[0]*scale)
# #     width = int(frame.shape[1]*scale)
# #     dimension = (width, height)
# #     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# # resize_img = resize_img_fun(img)
# # cv.imshow('resize_img',resize_img)
# # key = cv.waitKey(0)

# # if key == 27:
# #     cv.destroyAllWindows()

# def live_change_resolution (capture,width,height):
#     capture.set(3,width)
#     capture.set(4,height)

# live_change_resolution(capture,500,500)
# while True:
#     isTrue, frame = capture.read()
#     # resize_frame = resize_fun(frame)
#     # cv.imshow('resize_video',resize_frame)
#     cv.imshow('video',frame)
#     if cv.waitKey(20) & 0xFF ==ord('d'):
#         break


import cv2

def live_change_resolution(capture, width, height):
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Open the video capture
capture = cv2.VideoCapture(4)  # Use appropriate camera index (0, 1, 2, etc.)

# Set initial resolution (optional)
initial_width = 640
initial_height = 480
live_change_resolution(capture, initial_width, initial_height)

while True:
    # Read the frame from the video capture
    ret, frame = capture.read()

    # Perform any desired operations on the frame

    # Display the frame
    cv2.imshow('Video', frame)

    # Check for key press (wait for 1ms)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        # Change resolution to width=800, height=600
        live_change_resolution(capture, 200, 200)

# Release the video capture and close windows
capture.release()
cv2.destroyAllWindows()
