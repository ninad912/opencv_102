import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

para = [(15, 21, 4), (15, 42, 24), (15, 63, 41)]

for (d, sC, sS) in para:
    blurred = cv2.bilateralFilter(image, d, sC, sS)
    cv2.imshow("d = {} sC = {} sS = {}".format(d, sC, sS), blurred)
    cv2.waitKey(0)