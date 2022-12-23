import cv2 as cv
image=cv.imread('images/lion.jpg')

resized_image=cv.resize(image,(600,800),interpolation=cv.INTER_CUBIC)
#we use interpolation because when we are shrinking the images or enlarging the image it's quality doesn't tempare
cv.imshow('lion',image)
cv.imshow('lion2',resized_image)

#croping
crop=image[200:900,400:1000]#200:900 is pixel of height and 400:1000 is for height
cv.imshow('crop_image',crop)
cv.imwrite('crpeed_lion.jpg',crop)
#using write we can store image in drive
cv.waitKey(0)