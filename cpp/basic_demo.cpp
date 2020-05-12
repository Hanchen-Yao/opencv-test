//基本操作：加载图片、修改图片和保存图片
//作者：hanchen
//时间：2020年5月5日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>

using namespace cv;
int main(int argc, char** argv) {
	Mat src = imread("D:/opencv_exercises-master/images/02.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
			return -1;
	}
	//加载
	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);
	imshow("test opecv setup", src);
	
	//修改图像的色彩空间
	namedWindow("out put windows:", CV_WINDOW_AUTOSIZE);
	Mat output_image;
	cvtColor(src, output_image, CV_BGR2HLS);
	imshow("output windows", output_image);
	
	//保存
	imwrite("D:/opencv_exercises-master/images/03.jpg", output_image);
	waitKey(0);
	return 0;
}
