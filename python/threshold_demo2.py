# 超大图像二值化：分块、局部阈值和全局阈值
# 作者：hanchen
# 时间：2020年5月17日

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row: row+ch, col: cw+col]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row: row + ch, col: cw + col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("D:/opencv_exercises-master/images/result_001.jpg", gray)

print("----------Hello World!----------")
src = cv.imread("D:/opencv_exercises-master/images/big_image.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()
