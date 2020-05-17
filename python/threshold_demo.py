# 图像二值化：介绍了3种二值化的方法
# 作者：hanchen
# 时间：2020年5月17日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value %s"%ret)
    cv.imshow("binary", binary)

def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary", binary)

def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)  # 求出整个灰度图像的平均值
    print("mean:", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("threshold_custom", binary)

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/dave.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#threshold_demo(src)
#local_threshold(src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
