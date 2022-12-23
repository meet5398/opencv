import cv2 as cv
image1=cv.imread('images/IMG_3323.jpeg') #imread is used for reading the image
# in function we are taking image and  their height and width we want 
# here below image is just an variable you can take any variaable in place of image
#we are declaring w and h below for width and height 
def rescaleimage(image,w=0.50,h=0.12): # creating function rescaleFrame for rescaling image
    width = int(image.shape[1]*w)#frame.shape[1] means for width //we are using int for converting image dimensions into integer as we have taken above height and width into integer
    height=int(image.shape[0]*h) # [0] is for height
    dimensions= (width,height)
    return cv.resize(image,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleimage(image1)
cv.imshow('IMG_3323',resized_image) # imshow is used to show the images or u can say for the display images
cv.waitKey(0) #it is used to delay to open image window (if it is 0 it will close on pressing any key )


 
