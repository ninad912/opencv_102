import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))

tHat = cv2.morphologyEx(gray.copy(), cv2.MORPH_TOPHAT, rectKernel)
cv2.imshow("License Number", tHat)
cv2.waitKey(0)

bHat = cv2.morphologyEx(gray.copy(), cv2.MORPH_BLACKHAT, rectKernel)
cv2.imshow("License Plate", bHat)
cv2.waitKey(0)