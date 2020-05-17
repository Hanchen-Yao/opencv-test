# 直方图反向投影：HSV和RGB色彩空间
# 作者：hanchen
# 时间：2020年5月17日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def back_project_demo(): #反向投影
    sample = cv.imread("D:/opencv_exercises-master/images/messi1.jpg")
    target = cv.imread("D:/opencv_exercises-master/images/messi5.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    #show images
    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [36, 48], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)


def hist2d_demo(image): #绘制2D直方图
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0,1], None, [180, 256], [0, 180, 0,    256])
    #cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/Crystal.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
#cv.imshow("input image", src)
hist2d_demo(src)
back_project_demo()
cv.waitKey(0)
cv.destroyAllWindows()
