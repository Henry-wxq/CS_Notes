package com.henryw.object;

/**
 * 面向对象编程：先创建一个类结构，开发一个个对象，把数据交给对象，再调用对象的方法来完成对数据的处理
 * Test.java
 */

public class Student {
    // 打印学生总成绩，平均成绩
    // 先定义变量
    String name; // 姓名
    double chinese; // 语文成绩
    double math; // 数学成绩

    // 然后定义方法
    public void printTotalScore() {
        System.out.println(name + "的总成绩是: " + (chinese + math));
    }

    public void printAverageScore() {
        System.out.println(name + "的平均成绩是: " + (chinese + math) / 2);
    }
}
