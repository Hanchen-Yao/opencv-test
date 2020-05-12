//图像操作：单通道、三通道的图像和像素处理
//作者：hanchen
//时间：2020年5月9日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>
#include<math.h>

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
    Mat src, gray_src;
    src = imread("D:/images/lena.jpg");
    if (src.empty()) {
        cout << "could not load image..." << endl;
        return -1;
    }
    namedWindow("input", CV_WINDOW_AUTOSIZE);
    imshow("input", src);

    cvtColor(src, gray_src, CV_BGR2GRAY); //把图像src变成灰度图像gray_src
    namedWindow("output", CV_WINDOW_AUTOSIZE);
    imshow("output", gray_src);

    //单通道
    int height = gray_src.rows; //获取高度
    int width = gray_src.cols; //获取宽度
    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width; col++) {
            int gray = gray_src.at<uchar>(row, col);
            gray_src.at<uchar>(row, col) = 255 - gray; //反差图片
        }
    }

    //三通道
    Mat dst;
    dst.create(src.size(), src.type());
    height = src.rows;
    width = src.cols;
    int nc = src.channels(); //获取通道数
    
    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width; col++) {
            if(nc == 1){
            int gray = gray_src.at<uchar>(row, col);
            gray_src.at<uchar>(row, col) = 255 - gray;
            }
            else if(nc == 3){
                int  b = src.at<Vec3b>(row, col)[0];
                int  g = src.at<Vec3b>(row, col)[1];
                int  r = src.at<Vec3b>(row, col)[2];
                dst.at<Vec3b>(row, col)[0] = b;
                dst.at<Vec3b>(row, col)[1] = 0;
                dst.at<Vec3b>(row, col)[2] = r;

                gray_src.at<uchar>(row, col) = max(r, max(b, g)); //取灰度的另一种方法
            }
        }
    }
    
    //bitwise_not(src, dst); //反位操作

    //imshow("gray invert",dst);
    imshow("output", gray_src);
    waitKey(0);
    return 0;
}
