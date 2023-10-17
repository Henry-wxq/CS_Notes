package com.henryw.encapsulation;

/**
 * 面向对象的三大特征：封装，继承，多态
 *
 * 封装：用类设计对象处理某一个事物的数据时，应该要把处理的数据，以及处理这些数据的方法，设计到一个对象中去
 * 合理隐藏(public)，合理暴露(private)
 * private：在外部的文件无法访问内部的数据和方法，也无法赋值
 * 通常，定义赋值方法，我们用set开头，返回值我们用get开头
 */

public class Student {
    // 类中的变量隐藏的时候若有需要，需要创建set...方法和get...方法
    private double score;

    public void setScore(double score) {
        if (score >= 0 && score <= 100) {
            this.score = score;
        } else {
            System.out.println("数据非法");
        }
    }

    public double getScore() {
        return score; // 可以访问，因为在程序类中
    }

    // 需要被外界访问就用public，不需要被外界访问就用private
    public void printPass() {
        System.out.println(score >= 60 ? "成绩及格" : "成绩不及格");
    }
}
