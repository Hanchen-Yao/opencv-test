# 轮廓发现：findCounters发现轮廓、drawCounters绘制轮廓
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

    # edge_output = cv.Canny(grad_x, grad_y, 30, 150)
    edge_output = cv.Canny(gray, 30, 100)
    cv.imshow("Canny", edge_output)
    return edge_output

def countours_demo(image):
    '''
    dst = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    '''
    binary = edge_demo(image)
    countours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, countour in enumerate(countours):
        cv.drawContours(image, countours, i, (0, 0, 255), -1)
        print(i)

    cv.imshow("detect contours", image)

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/subpixel5.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
