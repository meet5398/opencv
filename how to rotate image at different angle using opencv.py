import cv2 as cv
import numpy as np

image= cv.imread('images/lion.jpg')
image=cv.resize(image,(400,400))
cv.imshow('lion',image)
#rotation
def rotate(image,angle,rotpoint=None):
    (height,width) = image.shape[:2] # here we know that 0 is for height and 1 for width so we are taking shape[:2]
    if rotpoint is None:
      rotpoint= (width/2,height/2)
    rotation_matrix=cv.getRotationMatrix2D(rotpoint,angle,1.0)# here 1 defined rotation scale of an image with respect to original image  
    dimensions = (width,height)
    return cv.warpAffine(image,rotation_matrix,dimensions)
# for rotating image in clockwise we  have to give angle in (-)
rotated_image=rotate(image,30)
cv.imshow('rotated_image',rotated_image)
cv.waitKey(0)
