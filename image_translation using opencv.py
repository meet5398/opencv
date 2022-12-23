import cv2 as cv
import numpy as np

image= cv.imread('images/lion.jpg')
image=cv.resize(image,(500,500))
cv.imshow('lion',image)

#translation (shifting an image along x or y axis ..left/right  top/bottom)
def translate(image,x,y):
    translate_matrix=np.float32([[1 , 0 , x] , [0 , 1 , y]])# x and y are shifting pixel on x axis and y axis respectively(how much we want to shift)
    print(type(np.float32(23.4563)))
    print(type(translate_matrix))
    dimensions= (image.shape[1],image.shape[0])
    print(type(dimensions))
    return cv.warpAffine(image,translate_matrix,dimensions)
#-x--> left shift
#-y ->> up
#x-->>right
#y-->down shift
translated=translate(image,100,200)
cv.imshow('translated', translated)
cv.waitKey(0)