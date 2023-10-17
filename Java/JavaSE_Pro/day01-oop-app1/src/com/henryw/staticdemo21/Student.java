package com.henryw.staticdemo21;

/**
 * 类方法的应用场景：做工具类，即一整个类都是类方法，每个方法都是用来完成一个功能的，工具类是给开发人员共同使用的
 * 提高了代码的复用，调用方便，可以使用类名直接调用类方法，提高了开发效率
 *
 */

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
