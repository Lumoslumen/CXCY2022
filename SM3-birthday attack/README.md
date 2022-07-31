project：

A.项目代码说明
分为sm3和生日攻击两部分
sm3部分：
通过国家密码管理局所发布的SM3密码杂凑算法，写出代码
https://oscca.gov.cn/scSM3密码杂凑算法a/xxgk/2010-12/17/1002389/files/302a3ada057c4a73830536d03e683110.pdf
经过填充和迭代压缩，生成杂凑值，杂凑值长度为256比特。


生日攻击部分：
参考
https://blog.csdn.net/Metal1/article/details/79887252
1.随机在2^(n/2)信息空间中寻找一个M
2.求出相应的tag
3.寻找是否有碰撞，没有则返回步骤1

具体代码解释见代码注释


B.运行指导

通过改变Birthdayattack(28)中n的值改变碰撞的bit数，直接运行即可。

C.代码运行过程截图

以28bit为例
<img src=">
