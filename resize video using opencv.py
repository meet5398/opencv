import cv2 as cv
#for reading(capturing) the video we are using VideoCapture
#video = cv.VideoCapture(0) #0 is used for giving priority if system using different webcam
#for displaying video we will apply while loop to display it frame by frame
#resizing the video dimensions
def rescalevideo(video,w=0.6,h=0.7):
    width = int(video.shape[1]  * w) #here w is width 
    height = int(video.shape[0] * h) # and here h is height     
    dimensions=(width,height)
    return cv.resize(video,dimensions,interpolation=cv.INTER_AREA)
video1 = cv.VideoCapture('video.mp4')

while True:
    isTrue,frame=video1.read()  # reading video in frame
    resized_video = rescalevideo(frame) #applying video frame by frame for resizing
    cv.imshow('video1',frame)
    cv.imshow('video resize',resized_video) #here video resize is name of video we are giving to it
    if cv.waitKey(20) & 0xff==ord('c'):# 0xff==ord('d') means that if you press d then it will close
     break;
video1.release() # for release the space occupied by video variable 
cv.destroyAllWindows()# close all the windows open from the code
