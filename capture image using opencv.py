import cv2 as cv
#for reading(capturing) the video we are using VideoCapture
image= cv.VideoCapture(0) #0 is used for giving priority if system using different webcam
result=True
# we have to click only 1st frame of an video so 
#we will make result false after 1st frame capture
while(result):
    isTrue,frame=image.read() # reading video in frame
    cv.imwrite('image1.jpg',frame) #displaying video in frame by frame
    cv.imshow('image1.jpg',frame)
    result=False
cv.waitKey(0)
#gpu is graphic processing unit
image.release() # for release the space occupied by video variable 
cv.destroyAllWindows()# close all the windows open from the code