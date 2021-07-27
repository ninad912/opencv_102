import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="hp.jpg",
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.waitKey(0)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

#Normal/Average Blur using the specified kernel size
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("[{}, {}] Blur".format(kX, kY), blurred)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cv2.imshow("Original", image)

#Gaussian Blur using the specified kernel size
for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("[{}, {}] Gaussian Blur".format(kX, kY), blurred)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cv2.imshow("Original", image)

#Median Blur only square shaped kernels to be used
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("{} Median Blur".format(k), blurred)
    cv2.waitKey(0)