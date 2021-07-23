import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="srk.jpg",
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Displaying RGB channels of the image individually
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name,chan)
    cv2.waitKey(0)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

#Converting RGB image to HSV image and then dispalying HSV channels individually
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.imshow("HSV Image", hsv)
cv2.waitKey(0)

for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name,chan)
    cv2.waitKey(0)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

#Converting RGB image to L*a*b* image and then dispalying L*a*b* channels individually
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.imshow("L*a*b* Image", lab)
cv2.waitKey(0)

for (name, chan) in zip(("L", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name,chan)
    cv2.waitKey(0)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

#Converting RGB image into a grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
