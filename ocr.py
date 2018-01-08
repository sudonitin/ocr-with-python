
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "-C:/Python27/test.png", required=True)
ap.add_argument("-p", "-thresh", type=str, default="thresh")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["-C:/Python27/test.png"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(a.txt, gray)


****OTHER CODE****
from PIL import Image
import pytesseract

Image.open("test.png")

pytesseract.image_to_string(Image.open("C:/Python27/test.png"))
