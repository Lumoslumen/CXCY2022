project：do your best to optimize SM3 implementation (software)

A.项目代码说明

SM3.cpp代码以
https://blog.csdn.net/nicai_hualuo/article/details/121555000
中代码为基础略做改动，用来做时间的参照

SM3.py中代码是独立完成

通过国家密码管理局所发布的SM3密码杂凑算法，写出代码

https://oscca.gov.cn/sca/xxgk/2010-12/17/content_1002389.shtml


经过填充和迭代压缩，生成杂凑值，杂凑值长度为256比特。


两者都用相同的ascill码，用256bit数据测试


B.运行指导

两者都可直接运行

C.代码运行过程截图

用256bit数据测试

C++代码


<img src="https://github.com/Lumoslumen/CXCY2022/blob/main/SM3-optimize/c.jpg" width="180" height="105">
>
python代码


<img src="https://github.com/Lumoslumen/CXCY2022/blob/main/SM3-birthday%20attack/birthday.jpg" width="180" height="105">
>
