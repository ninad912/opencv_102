import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Converting image to grayscale and blurring
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

#Applying Binary Inverse Threshold with Otsu_Threshold flag
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print("Threshold value computed by THRESH_OTSU flag = {}".format(T))
cv2.imshow("Binary Inverse Threshold", threshInv)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = threshInv)
cv2.imshow("After msking", masked)
cv2.waitKey(0)
