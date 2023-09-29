package com.henryw.object;

/**
 * 对象本质上是一种特殊的数据结构，下面相当于是创建了s1和s2的学生表
 */

public class Test {
    public static void main(String[] args) {
        // 1. 创建一个学生对象，封装波妞数据
        Student s1 = new Student();
        s1.name = "波妞";
        s1.chinese = 100;
        s1.math = 100;

        // 调用方法
        // 因为是通过s1调用的，只会使用s1里面的数据
        s1.printTotalScore();
        s1.printAverageScore();

        // 2. 再创建一个学生对象，封装波仔数据
        Student s2 = new Student();
        s2.name = "波仔";
        s2.chinese = 59;
        s2.math = 100;

        s2.printTotalScore();
        s2.printAverageScore();

    }
}
