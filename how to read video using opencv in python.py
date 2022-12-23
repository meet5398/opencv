import cv2 as cv
#for reading(capturing) the video we are using VideoCapture
#video = cv.VideoCapture('video.mp4')
video = cv.VideoCapture(0) #0 is used for giving priority if system using different webcam
#for displaying video we will apply while loop to display it frame by frame
while True:
    isTrue,frame=video.read() # reading video in frame
    cv.imshow('video',frame) #displaying video in frame by frame
    if cv.waitKey(20) & 0xff==ord('c'):# 0xff==ord('d') means that if you press d then it will close
        break;
video.release() # for release the space occupied by video variable 
cv.destroyAllWindows()# close all the windows open from the code