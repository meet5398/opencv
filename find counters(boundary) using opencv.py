import cv2 as cv
import numpy as np

image=cv.imread('images/lion.jpg')
image=cv.resize(image,(500,500))
cv.imshow('lion',image)
blank= np.zeros(image.shape,dtype='uint8')
cv.imshow('blank',blank)

#1st we will convert it into gray scale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur image before find counters
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

 # now conver it into edges
edges=cv.Canny(blur,125,175)
cv.imshow('edges',edges)

#now we will find no of contours in images
contours,hierarchies =cv.findContours(edges,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
 #there are cv.RETR_LIST--> for printing all contours
  #         cv.RETR_TREE --> for printing in hierarchical Order
 #          cv.RETR_EXTERNAL --> for printing external counters
print(len(contours))
 #now we will draw_contours
cv.drawContours(blank,contours,-1,(0,0,255),1)
#here -1 is for index here we are all countors so we have declared it -1
# and here 3 is thickness
cv.imshow('drawn_counters',blank)

cv.waitKey(0)