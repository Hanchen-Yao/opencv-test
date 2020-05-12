//Mat对象:通过Mat处理图片
//作者：hanchen
//时间：2020年5月9日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>
#include<math.h>

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
    Mat src;
    src = imread("D:/images/lena.jpg");
    if (src.empty()) {
        cout << "could not load image..." << endl;
        return -1;
    }
    namedWindow("input", CV_WINDOW_AUTOSIZE);
    imshow("input", src);

    /*
    Mat dst; //创建一个空白图片
    dst= Mat(src.size(), src.type());
    dst = Scalar(127, 0, 255); //选择一个颜色
    namedWindow("output", CV_WINDOW_AUTOSIZE);
    imshow("output", dst);
    */
    
    //克隆图片
    //Mat dst = src.clone;
    Mat dst;
    //src.copyTo(dst);
    namedWindow("output", CV_WINDOW_AUTOSIZE);


    cvtColor(src, dst, CV_BGR2GRAY); //输出的图像为单通道
    printf("input image channels : %d\n", src.channels());
    printf("output image channels : %d\n", dst.channels());

    int cols = dst.cols;
    int rows = dst.rows;
    printf("rows : %d cols : %d\n", rows, cols); //输出行数和列数
    const uchar* firstRow =dst.ptr<uchar>(0); //输出第一个灰度值
    printf("first pixel value : %d\n", *firstRow);

    //创建一个小图像
    Mat M(100, 100, CV_8UC3, Scalar(0, 0, 255)); 
    cout << "M = " << endl << M << endl;

    //定义一个小数组
    Mat csrc;
    Mat kernel = (Mat_<float>(3,3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
    filter2D(src, csrc, -1, kernel); //通过数组对图像进行滤波

    Mat m2 = Mat::zeros(src.size(), src.type()); //创建一个黑色图像

    imshow("output", m2);
    waitKey(0);
    return 0;
}
