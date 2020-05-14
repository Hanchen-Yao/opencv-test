# 边缘保留滤波：高斯双边和均值迁移
# 作者：hanchen
# 时间：2020年5月14日
import cv2 as cv
import numpy as np

def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)

def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/example.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
