//filter 2D:矩阵的掩膜操作
//作者：hanchen
//时间：2020年5月7日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>
#include<math.h>

using namespace cv;

int main(int argc, char** argv) {
	Mat src, dst;
	src = imread("D:/images/lena.jpg"); //输入图片
	if (!src.data) { //判断是否输入图片成功
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input image", CV_WINDOW_AUTOSIZE);
	imshow("input image", src);

	/*
	//获取图像高度和宽度
	int cols = (src.cols - 1) * src.channels(); //图像的宽度
	int offsetx = src.channels();
	int rows = src.rows; //图像的高度
	dst = Mat::zeros(src.size(), src.type());
	for (int row = 1; row < (rows - 1); row++) {
	 	 const uchar* previous = src.ptr<uchar>(row - 1);
		 const uchar* current = src.ptr<uchar>(row);
		 const uchar* next = src.ptr<uchar>(row + 1);
		 uchar* output = dst.ptr<uchar>(row);
		 for (int col = offsetx; col < cols; col++) { //像素范围处理
		 output[col] = saturate_cast<uchar>(5 * current[col] - (current[col - offsetx] + current[col + offsetx] + previous[col] + next[col]));
		}
	}
	*/

	Mat kernel = (Mat_<char>(3, 3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
	filter2D(src, dst, src.depth(), kernel);//函数调用filter 2D功能
	
	namedWindow("contrast image demo", CV_WINDOW_AUTOSIZE);
	imshow("contrast image demo", dst);

	waitKey(0);
	return 0;
}
