package com.henryw.thisdemo;

/**
 * this就是一个变量，可以用在方法中，来拿到当前对象
 *
 * this的应用场景：解决变量名称冲突问题，在形参和实参名称一样时，在形参前加上this
 */

public class Student {
    // 学生成绩是否高于录取分数线
    double score;

    public void printThis() {
        System.out.println(this);
    }

    public void printPass(double score) {
        if (this.score > score) {
            System.out.println("通过啦");
        } else {
            System.out.println("落选了");
        }

        System.out.println(this.score > score ? "通过啦" : "落选了"); // 优化代码
    }
}
