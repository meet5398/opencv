#pip install caer is used for speed up the performance
import cv2 as cv
image=cv.imread('images/IMG_3323.jpeg') #imread is used for reading the image
cv.imshow('IMG_3323',image) # imshow is used to show the images or u can say for the display images
cv.waitKey(0) #it is used to delay to open image window (if it is 0 it will close on pressing any key )


