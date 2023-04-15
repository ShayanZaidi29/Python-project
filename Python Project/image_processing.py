# import cv2
# # img=cv2.imread("Dracula.png")
# img2=cv2.imread("Nature.jpg")

# original image

# import cv2
# cv2.imshow('Original Image', img) 
# cv2.waitKey(0)

# # image resize

# newImg = cv2.resize(img2, (0,0), fx=0.75, fy=0.75)
# cv2.imshow('Resized Image', newImg)
# cv2.waitKey(0)

# #Centroid

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Centroid', gray_img)
# cv2.waitKey(0)

# Rotate an image

# height, width = img.shape[0:2]
# rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
# rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
# cv2.imshow('Rotate', rotatedImage)
# cv2.waitKey(0)

#Image BLur(Median Blur)

# blur_image = cv2.medianBlur(img2,5)
# cv2.imshow('Original Image', img2)
# cv2.imshow('Blur Image', blur_image)
# cv2.waitKey(0)

#Background remover
import cv2
img=cv2.imread("bulb.jpg",0)
import numpy as np
gray_img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
_,thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
img_contours = sorted(img_contours, key=cv2.contourArea)
for i in img_contours:
    if cv2.contourArea(i) > 100:
        break
mask = np.zeros(img.shape[:2], np.uint8)
cv2.drawContours(mask, [i],-1, 255, -1)
new_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Image with background removed", new_img)
cv2.waitKey(0)
