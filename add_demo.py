#像素运算：对两张图片进行加减乘除
#作者：hanchen
#时间：2020年5月5日

import cv2 as cv

def add_demo(m1, m2):#两张图片相加
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)

def subtract_demo(m1, m2):#两张图片相减
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)

def divide_demo(m1, m2):#两张图片相除
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2):#两张图片相乘
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)

def others(m1, m2):#均值统计
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
src1 = cv.imread("D:/opencv_exercises-master/images/01.jpg")#读取第一张图片
src2 = cv.imread("D:/opencv_exercises-master/images/02.jpg")#读取第二张图片
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
#add_demo(src1, src2)
#subtract_demo(src1, src2)
#divide_demo(src1, src2)
#multiply_demo(src1, src2)
others(src1, src2)

cv.waitKey(0)
cv.destroyAllWindows()
