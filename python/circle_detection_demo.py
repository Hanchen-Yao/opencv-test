# 圆检测：霍夫圆检测
# 作者：hanchen
# 时间：2020年5月18日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def detect_circle_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    print(circles.shape)
    for i in circles[0, :]:  # draw the outer circle
        cv.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)  # draw the center of the circle
        cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv.imshow('detected circles', image)

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
detect_circle_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
