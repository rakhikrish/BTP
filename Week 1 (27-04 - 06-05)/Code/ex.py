import glob
import cv2
import imutils

images = [cv2.imread(file) for file in glob.glob("*.png")]
img=images[0]
image='image'
image1='bwimage'
image2='rot_image'
image3='crop_image'
cv2.imshow(image,img) 
gimg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
(thresh, bwimg) = cv2.threshold(gimg, 127, 255, cv2.THRESH_BINARY)
cv2.imshow(image1,bwimg)
rtimg=imutils.rotate(img,angle=270)
cv2.imshow(image2,rtimg)
crop=img[0:100,0:100]
cv2.imshow(image3,crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
