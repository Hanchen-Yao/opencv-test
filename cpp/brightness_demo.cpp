//调整亮度:通过对每个通道每个像素赋值，改变图像的亮度和对比度
//作者：hanchen
//时间：2020年5月9日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>
#include<math.h>

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
    Mat src, dst;
    src = imread("D:/images/lena.jpg");
    if (!src.data) {
        printf("could not load image...");
        return -1;
    }
    char input_win[] = "input image"; //定义一个变量表示title
    namedWindow(input_win, CV_WINDOW_AUTOSIZE);
    imshow(input_win, src);

    //图像亮度调整
    int height = src.rows;
    int width = src.cols;
    dst = Mat::zeros(src.size(), src.type());
    float alpha = 1.5;
    float beta = 30;

    Mat m1;
    src.convertTo(m1, CV_32F); //将src转变为m1
    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width; col++) {
            if (src.channels() == 3) {
                float b = m1.at<Vec3f>(row, col)[0]; //blue
                float g = m1.at<Vec3f>(row, col)[1]; //green
                float r = m1.at<Vec3f>(row, col)[2]; //red

                //saturate_cast<uchar>(）确保值的大小在0~255范围
                //给每个像素点每个通道赋值
                dst.at<Vec3b>(row, col)[0] = saturate_cast<uchar>(b * alpha + beta);
                dst.at<Vec3b>(row, col)[1] = saturate_cast<uchar>(g * alpha + beta);
                dst.at<Vec3b>(row, col)[2] = saturate_cast<uchar>(r * alpha + beta);
            }
            else if (src.channels() == 1) {
                float v = src.at<uchar>(row, col);
                dst.at<uchar>(row, col) = saturate_cast<uchar>(v * alpha + beta);
            }
        }
    }
        
    char output_title[] = "contrast and brightness change demo";
    namedWindow(output_title, CV_WINDOW_AUTOSIZE);
    imshow(output_title, dst);
    waitKey(0);
    return 0;
}
