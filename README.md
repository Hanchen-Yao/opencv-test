# opencv-test
学习OpenCV课程的时候做的一些程序测验。  
## pythom风格  
1. add_demo.py  
像素运算：对两张图片进行加减乘除。  
* add_demo()——两张图片相加；  
* subtract_demo()——两张图片相减；  
* divide_demo()——两张图片相除；  
* multiply_demo()——两张图片相乘；  
* others()——均值统计；
2. add_demo2.py  
像素运算2：逻辑运算和亮度增强。  
* logic_demo()——逻辑运算与或非；  
* contrast_brightness_demo()——增强对比度；  
3. roi_demo.py  
ROI与泛洪填充：换掉图片区域的某个部分。  
* fill_color_demo()——颜色填充；  
* fill_binary()——选取一个mask换掉目标图片。  
## c++风格 
1. basic_demo.cpp  
基本操作：加载图片、修改图片和保存图片。  
* imread——加载图片；
* imshow——显示图片；  
* cvtColor——修改色彩空间；  
* imwrite——保存图片；  
