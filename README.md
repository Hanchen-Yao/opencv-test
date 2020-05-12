# opencv-test
学习OpenCV课程的时候做的一些程序测验。  
## pythom风格  
1. add_demo.py  
像素运算：对两张图片进行加减乘除。  
* add_demo()——两张图片相加  
* subtract_demo()——两张图片相减  
* divide_demo()——两张图片相除  
* multiply_demo()——两张图片相乘  
* others()——均值统计
2. add_demo2.py  
像素运算2：逻辑运算和亮度增强。  
* logic_demo()——逻辑运算与或非  
* contrast_brightness_demo()——增强对比度  
3. roi_demo.py  
ROI与泛洪填充：换掉图片区域的某个部分。  
* fill_color_demo()——颜色填充  
* fill_binary()——选取一个mask换掉目标图片  
## c++风格 
1. basic_demo.cpp  
基本操作：加载图片、修改图片和保存图片。  
* imread——加载图片
* imshow——显示图片  
* cvtColor——修改色彩空间  
* imwrite——保存图片  
2. bgr_demo.cpp  
图像操作：单通道、三通道的图像和像素处理。    
* 单通道  
* 三通道  
3. brightness_demo.cpp  
调整亮度:通过对每个通道每个像素赋值，改变图像的亮度和对比度。    
4. detect_lines_demo.cpp  
直线检测：用形态学的方法提取英语试卷填空题的下划线。
* 霍夫直线检测  
* 形态学操作  
5. filter2d_demo.cpp  
Filter 2D:矩阵的掩膜操作。  
* 获取图像高度和宽度  
* 函数调用filter 2D功能
6. hline_demo.cpp  
形态学操作应用：提取垂直线和水平线。
* 彩色图像转为灰度图像  
* 灰度图像转为二值图像
* 膨胀和腐蚀
* 开操作
7. mat_demo.cpp  
Mat对象:通过Mat处理图。  
* 克隆图片  
* 创建小图
* 创建数组
8. open_demo.cpp 
open操作：开操作，先腐蚀后膨胀。  
9. show_demo.cpp
显示图片：显示一张指定图片。  

