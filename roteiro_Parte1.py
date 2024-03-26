import cv2
import numpy as np

# read the input image
img = cv2.imread('trabalhoPDI.png')

# access the height and width of image
height,width, _ = img.shape

# define the translation matrix
M = np.float32([[1,0,50],[0,1,50]])

# perform the translation
img = cv2.warpAffine(img,M,(width,height))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# display the translated image
cv2.imshow('Image HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Imagem HLS', hls)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Imagem Cinza', cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()