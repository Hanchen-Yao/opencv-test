# ROI与泛洪填充：换掉图片区域的某个部分
# 作者：hanchen
# 时间：2020年5月10日

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    # 参数：原图，mask图，起始点，起始点值减去该值作为最低值，起始点值加上该值作为最高值，彩色图模式
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImg)

def fill_binary(image):
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0

    cv.floodFill(image, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)

if __name__ == '__main__':
    print("----------Hello World!----------")
    src = cv.imread("D:/opencv_exercises-master/images/a_zhu.jpg")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    #cv.imshow("input image", src)
    """
       fill_color_demo(src)
       face = src[50:250, 100:300]
       gray = cv.cvtColor(face,cv.COLOR_RGB2GRAY)
       blackface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
       src[50:250, 100:300] = blackface
       #cv.imshow("gray", gray)
       cv.imshow("blackface", src)
   """
    cv.waitKey(0)
    cv.destroyAllWindows()
