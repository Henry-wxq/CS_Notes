package com.henryw.object;

/**
 *
 */

public class Student {
    // 打印学生总成绩，平均成绩
    String name;
    double chinese;
    double math;

    public void printTotalScore() {
        System.out.println(name + "的总成绩是：" + (chinese + math));
    }

    public void printAverageScore() {
        System.out.println(name + "的平均成绩是" + (chinese + math) / 2);
    }
}
