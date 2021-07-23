import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#applying a series of erosions
for i in range(0,3):
    eroded = cv2.erode(gray.copy(), None, iterations = i + 1)
    cv2.imshow("Eroded {} Times".format(i+1), eroded)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cv2.imshow("Original",image)
    
#applying a series of dilation
for i in range(0,3):
    dilated = cv2.dilate(gray.copy(), None, iterations = i + 1)
    cv2.imshow("Dilated {} Times".format(i+1), dilated)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cv2.imshow("Original",image)

kernelSizes = [(2, 2), (4, 4), (6, 6)]

#Opening operation over the specified kernel sizes
for kernsize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernsize)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening over [{}, {}]".format(kernsize[0], kernsize[1]), opening)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cv2.imshow("Original",image)
    
#Closing operation over the specified kernel sizes
for kernsize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernsize)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing over [{}, {}]".format(kernsize[0], kernsize[1]), closing)
    cv2.waitKey(0)