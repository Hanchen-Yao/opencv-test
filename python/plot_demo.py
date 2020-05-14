# 图像直方图：观察图像特征
# 作者：hanchen
# 时间：2020年5月14日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image],[i], None, [256], [0,256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/example.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()
