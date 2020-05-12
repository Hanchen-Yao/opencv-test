//形态学操作应用：提取垂直线和水平线
//作者：hanchen
//时间：2020年5月10日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>
#include<math.h>

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
    Mat src, dst;
    src = imread("D:/images/0510.jpg");
    if (!src.data) {
        printf("could not load image...\n");
        return -1;
    }
   
    char INPUT_WIN[] = "input image";
    char OUTPUT_WIN[] = "result image";
    namedWindow(INPUT_WIN, CV_WINDOW_AUTOSIZE);
    imshow(INPUT_WIN, src);

    //彩色图像转为灰度图像
    Mat gray_src;
    cvtColor(src, gray_src, CV_BGR2GRAY);
    imshow("gray image", gray_src);
 
    //灰度图像转为二值图像
    Mat binImg;
    adaptiveThreshold(~gray_src, binImg, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 15, -2);
    imshow("binary image", binImg);

    //水平结构元素
    Mat hline = getStructuringElement(MORPH_RECT, Size(src.cols /16, 1), Point(-1, -1));
    //垂直结构元素
    Mat vline = getStructuringElement(MORPH_RECT, Size(1, src.rows / 16), Point(-1, -1));
    //矩形结构
    Mat kernel = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));
    Mat temp; //膨胀和腐蚀
    erode(binImg, temp, hline);
    dilate(temp, dst, hline);
    //morphologyEx(binImg, dst, CV_MOP_OPEN, vline); //开操作
    bitwise_not(dst, dst);
    blur(dst, dst, Size(3, 3), Point(-1, -1));
    imshow("Final Result", dst);

    waitKey(0);
    return 0;
}
