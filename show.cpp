//显示图片：显示一张指定图片
//作者：hanchen
//时间：2020年5月5日

#include<opencv2/opencv.hpp>
#include <opencv2/highgui/highgui_c.h>
#include<iostream>

using namespace cv;
int main(int argc, char** argv) {
	Mat src = imread("D:/opencv_exercises-master/images/01.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
			return -1;
	}
	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);
	imshow("test opecv setup", src);

	waitKey(0);
	return 0;
}
