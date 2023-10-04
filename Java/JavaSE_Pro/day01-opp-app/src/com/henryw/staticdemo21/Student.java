package com.henryw.staticdemo21;

public class Student {

    double score;

    // 类方法
    public static void printHelloWorld(){
        System.out.println("Hello World 1");
        System.out.println("Hello World 2");
    }

    // 实例方法
    public void printPass(){
        System.out.println("成绩" + (score >= 60 ? "及格" : "不及格"));
    }
}
