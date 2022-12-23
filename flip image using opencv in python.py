import cv2 as cv

image= cv.imread('images/lion.jpg')
cv.imshow('lion',image)
# 0 - means flip verticaly
# 1 - means flip horizontaly
#-1 - means flip horizontaly and vericaly
flip=cv.flip(image,-1)
#flip1=cv.flip(image,1 )
#flip2=cv.flip(image,-1 )
cv.imshow('flip',flip)
#cv.imshow('flip1',flip1)
#cv.imshow('flip2',flip2)
cv.waitKey(0)