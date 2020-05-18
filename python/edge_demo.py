# Canny边缘提取：高斯模糊、灰度转换、计算梯度、非最大信号抑制、高低阈值输出二值图像
# 作者：hanchen
# 时间：2020年5月18日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    edge_output = cv.Canny(grad_x, grad_y, 30, 150)
    #edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("gray", gray)
    cv.imshow("Canny demo", edge_output)

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/messi5.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
