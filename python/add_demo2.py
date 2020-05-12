# 像素运算2：逻辑运算和亮度增强
# 作者：hanchen
# 时间：2020年5月6日

import cv2 as cv
import numpy as np

def add_demo(m1, m2): #加法
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)

def subtract_demo(m1, m2): #减法
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)

def divide_demo(m1, m2): #除法
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2): #乘法
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)

def logic_demo(m1, m2): #逻辑运算之非运算
    dst = cv.bitwise_not(m1, m2)
    cv.imshow("logic_demo", dst)

def contrast_brightness_demo(image, c, b): #增强对比度
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("contrast_brightness_demo", dst)

def others(m1, m2): #均值统计
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)



print("------fighting------")
src1 = cv.imread("D:/opencv_exercises-master/images/01.jpg")
src2 = cv.imread("D:/opencv_exercises-master/images/02.jpg")
src3 = cv.imread("D:/opencv_exercises-master/images/a_zhu.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
cv.imshow("image3", src3)
#add_demo(src1, src2)
#subtract_demo(src1, src2)
#divide_demo(src1, src2)
#multiply_demo(src1, src2)--
#others(src1, src2)
#logic_demo(src1, src2)
contrast_brightness_demo(src3, 1.2, 10)

cv.waitKey(0)
cv.destroyAllWindows()
