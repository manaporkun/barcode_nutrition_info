from pyzbar import pyzbar
from PIL import Image
import cv2

import numpy as np
import argparse
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "path to the image file")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# compute the Scharr gradient magnitude representation of the images
# in both the x and y direction using OpenCV 2.4
ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

"""
info = pyzbar.decode(Image.open('etiket2.jpg'))
img = cv2.imread('etiket2.jpg')
info2 = pyzbar.decode(img)
print(info2, info)

def draw_barcode(decoded, image):
    start_point = (int(decoded.rect.left), int(decoded.rect.top))
    end_point = (int(decoded.rect.left + decoded.rect.width), int(decoded.rect.top + decoded.rect.height))
    # Blue color in BGR 
    color = (255, 0, 0) 
  
    # Line thickness of 2 px    
    thickness = 2

    image = cv2.rectangle(image, start_point, end_point, color, int(thickness))
    return image

for obj in info2:
    print("Type:", obj.type)
    print("Data:", obj.data)
    print()

    cv2.imshow('test', draw_barcode(obj, img))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""