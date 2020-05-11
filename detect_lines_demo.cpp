//直线检测：用形态学的方法提取英语试卷填空题的下划线
//作者：hanchen
//时间：2020年5月10日

#include<opencv2/opencv.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<iostream>
#include<math.h>

using namespace std;
using namespace cv;

int max_count = 255;
int threshold_value = 100;
const char* output_lines = "Hough Lines";
Mat src, roiImage, dst;
//void detectLines(int, void*);
void morphologyLines(int, void*);

int main(int argc, char** argv) {
    src = imread("D:/images/0511.png", IMREAD_GRAYSCALE);
    if (src.empty()) {
        printf("could not load image...\n");
        return -1;
    }
    namedWindow("input image", CV_WINDOW_AUTOSIZE);
    imshow("input image", src);
    namedWindow("output image", CV_WINDOW_AUTOSIZE);
    Rect roi = Rect(10, 10, src.cols -20, src.rows -20);
    roiImage = src(roi);
    //imshow("ROI image", roiImage);
    //createTrackbar("threshold:",output_lines, &threshold_value, max_count, detectLines);
    //detectLines(0, 0);
    morphologyLines(0, 0);
    waitKey(0);
    return 0;
}

//霍夫直线检测
/*
void detectLines(int, void*) {
    Canny(src, dst, threshold_value, threshold_value * 2, 3, false); //边缘提取
    //threshold(roiImage, dst, 0, 255, THRESH_BINARY | THRESH_OTSU); //二值化
    vector<Vec4i>lines;
    HoughLinesP(dst, lines, 1, CV_PI/180.0, 30, 30.0, 0);
    cvtColor(dst, dst, COLOR_GRAY2BGR);
    for (size_t t = 0; t < lines.size(); t++) {
        Vec4i ln = lines[t];
        line(dst, Point(ln[0], ln[1]), Point(ln[2], ln[3]), Scalar(0, 0, 255), 2, 8, 0);
    }
    imshow(output_lines, dst);
}
*/

//形态学操作
void morphologyLines(int, void*) {
    //binary image
    Mat binaryImage, morphImage;
    threshold(roiImage, binaryImage, 0 ,255,THRESH_BINARY_INV | THRESH_OTSU);
    imshow("binary result", binaryImage);

    //morphology opreation
    Mat kernel = getStructuringElement(MORPH_RECT, Size(20, 1), Point(-1, -1));
    morphologyEx(binaryImage, morphImage, MORPH_OPEN, kernel, Point(-1, -1));
    imshow("morphology result", morphImage);

    //dilate image
    kernel = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));
    dilate(morphImage, morphImage, kernel);
    imshow("morphology lines", morphImage);

    //hough lines
    vector<Vec4i>lines;
    HoughLinesP(morphImage, lines, 1, CV_PI / 180.0, 30, 20.0, 0);
    Mat resultImage = roiImage.clone();
    cvtColor(resultImage, resultImage, COLOR_GRAY2BGR);
    for (size_t t = 0; t < lines.size(); t++) {
        Vec4i ln = lines[t];
        line(resultImage, Point(ln[0], ln[1]), Point(ln[2], ln[3]), Scalar(0, 0, 255), 2, 8, 0);
    }
    imshow(output_lines, resultImage);
    return;
}   
