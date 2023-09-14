"""
1) Module: python中的模块，说白了就是python文件，python文件名一般为xxx.py，则模块的名字是xxx
2) Package: 可理解为一组module，一堆相关的module组成的
    a) 通常包是一个目录，可以使用import导入包，或者from+import导入包内的部分module
3) Library: 库，也常称为库文件； library常用语其它编程语言，如c, c++, 其中常见的有：
    a) 静态库文件: xxx.a
    b) 动态库文件：xxx.dll
4) Module和Library的区别：
    a) 都是提供了一定的功能供别人调用
    b) Python中的library等价于module；只不过Python中很少说library，正常情况下都说module
    c) library多数都是指的是C，C#等语言中的库，库文件；Python中很少用library这个词
    d) Python中的“库”称为“module”——模块
5) Module和Package的区别：
    a) 导入单个的module，一般是这样的：import my_module
        § module：单个的模块，一般是单个（偶尔为多个）python文件；
    b) 导入package一般是这样的: from my_package.timing.internets import function_of_love
        § package：多个相关的module的组合。肯定是多个，相关的Python文件的组合；Package是用来把相关的模块组织在一起，成为一个整体的
"""