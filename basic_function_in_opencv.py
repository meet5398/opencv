import cv2 as cv
image= cv.imread('images/lion.jpg')
image=cv.resize(image,(500,500))
cv.imshow('Lion',image)

#converting iamge  to grayscale
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray_image',gray)

#bluring the image
blur=cv.GaussianBlur(image,(3,3),cv.BORDER_DEFAULT) # here (3,3) is kernel size if we increase the size blurness will increase and it will be always in odd number
cv.imshow('blur_iamge',blur)

# edge cascade(edging the image)
edging=cv.Canny(image,125,175) # as we decrease the edging then we will get more edges but clearity will be decrease 
#we can reduce the iamge by blurring
cv.imshow('edging',edging)

#dilating the iamge
dilated = cv.dilate(edging,(5,5),iterations=3) #we are taking image which is already edged and (5,5) is kernel as defined above
cv.imshow('dilated',dilated)

#eroding(shrink,eating up the image)
eroded= cv.erode(dilated,(4,4),iterations=1)
cv.imshow('eroded',eroded)
 
cv.waitKey(0)

