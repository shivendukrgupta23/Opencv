
import cv2

#load the image
img = cv2.imread('photo/logo.png',1)

# -1,cv2.IMREAD_COLOR : loads a color image. 
# Any transparnecy of image will be negelected . It is the default flag.
# 0,cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode.
# 1,cv2.IMREAD_UNCHANGES: Loads image as such including aplha channel.



#  for resize the screen size
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) 

#for rotate teh images
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#for new file create and save the rotate images
cv2.imwrite('new_img.png',img) 



#this is used to display the image on the screen.
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
