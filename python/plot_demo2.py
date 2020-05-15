# 直方图应用：对比度增强，两个直方图作比较
# 作者：hanchen
# 时间：2020年5月15日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def equalHist_demo(image): #直方图均衡化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)

def calhe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("equalHist_demo", dst)

def create_rgb_demo(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1           
    return rgbHist

def hist_compare(image1, image2): #两个直方图作比较，如巴氏距离、相关性、卡方
    hist1 = create_rgb_demo(image1)
    hist2 = create_rgb_demo(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离:%s, 相关性:%s, 卡方:%s"%(match1, match2, match3))

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/dave.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
#cv.imshow("input image", src)
#calhe_demo(src)

image1 = cv.imread("D:/opencv_exercises-master/images/a_zhu.jpg")
image2 = cv.imread("D:/opencv_exercises-master/images/Crystal.jpg")
cv.imshow("image1", image1)
cv.imshow("image2", image2)
hist_compare(image1, image2)

cv.waitKey(0)
cv.destroyAllWindows()
