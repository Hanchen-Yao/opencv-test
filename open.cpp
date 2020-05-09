//open：开操作，先腐蚀后膨胀
//close：闭操作，先膨胀后腐蚀
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
        printf("could not load image...\n");
        return -1;
    }
    namedWindow("intput image", CV_WINDOW_AUTOSIZE);
    imshow("input image", src);
    char output_title[]= "morphology demo";
    namedWindow(output_title, CV_WINDOW_AUTOSIZE);

    Mat kernel = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));
    morphologyEx(src, dst, CV_MOP_OPEN, kernel);
    imshow(output_title, dst);
    imwrite("D:/images/lena2.jpg", dst);
 
    waitKey(0);
    return 0;
}
