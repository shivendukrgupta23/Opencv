import cv2 
import random

img = cv2.imread('photo/logo.png',-1)

#this is represent the  numpy.ndarray
#print(type(img))


#for change the pixel 
# for i in range(100):
#     for j in range(img.shape[1]):
#        img[i][j] = [random.randint(0,225), random.randint(0,225), random.randint(0,225)]

# this is copy some portion of images then paste this portion to another portion with ratio
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

