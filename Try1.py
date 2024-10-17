from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb

imagepath1 = '/Users/vaibhavrathore1999/Downloads/MS/EE 610 Image Processing/Assignments/comp_assgn2_images/low-contrast-photography-1.jpg'
imagecv = cv2.imread(imagepath1) #Importing Image
#Display image
plt.imshow(imagecv)
plt.show()

