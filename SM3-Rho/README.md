project：

A.项目代码说明

分为sm3和Rho两部分
sm3部分：
通过国家密码管理局所发布的SM3密码杂凑算法，写出代码

https://oscca.gov.cn/sca/xxgk/2010-12/17/content_1002389.shtml


经过填充和迭代压缩，生成杂凑值，杂凑值长度为256比特。


Rho部分：
参考
https://blog.csdn.net/jk_chen_acmer/article/details/81951490
当哈希值的前n bit出现在列表中时，说明发生碰撞

具体代码解释见代码注释


B.运行指导

通过改变Rho(32)中n的值改变碰撞的bit数，直接运行即可。

C.代码运行过程截图

以32bit为例
<img src="https://github.com/Lumoslumen/CXCY2022/blob/main/SM3-birthday%20attack/birthday.jpg" width="180" height="105">
>

