#IN this file we will draw line ,rectangle circle fill color and write text on the image
import cv2 as cv
import numpy as np
# for dreawing we can draw on blank image also by creating it or by on existing image also
blank=np.zeros((500,500,3), dtype='uint8')# we can create random blank image using this here 'unit8 is image data type, we will give 3 as size
cv.imshow('blankimage',blank)

#now we will paint the image
blank[:]= 0,255,0
cv.imshow('green',blank)

#now we will color particular portion of an image
blank[200:300,400:500]=0,0,255 # (height,width)
cv.imshow('red',blank)

#drawing a line
cv.line(blank,(200,300),(300,400),(256,0,0),thickness=5)
cv.imshow('line',blank)

#now we will draw rectangle
cv.rectangle(blank, (0,0) , (250,250), (250,0,0),thickness=2)
cv.imshow('rectangle',blank)

#now we can filled rectangle part by :
cv.rectangle(blank, (0,0) , (250,250), (250,0,0),thickness=cv.FILLED) #or by applying  thickness= -1
cv.imshow('rectangle',blank)

#now will dreaw circle
blank2=np.zeros((500,500,3), dtype='uint8')# we can create random blank image using this here 'unit8 is image data type, we will give 3 as size
cv.circle(blank2,(250,250),40,(0,250,250),thickness=4)
#you can try below method also for defining center
#we can filled image by as we have used for rectangle
#cv.circle(blank2,(blank2.shape[1]//2,blank2.shape[0]//2),40,(0,250,250),thickness=4)
cv.imshow('circle',blank2)


#how to put text in image
blank3=np.zeros((500,500,3), dtype='uint8')
cv.putText(blank3,'I love You',(100,100),cv.FONT_HERSHEY_TRIPLEX,2.0,(0,255,0),5)
cv.imshow('text',blank3)
cv.waitKey(0)