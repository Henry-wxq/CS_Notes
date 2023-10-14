package com.henryw.staticdemo21;

public class Test {
    // main方法是个类方法
    // 通过虚拟机调类名完成Test.main()来执行的
    public static void main(String[] args) {
        // 1. 类方法的用法
        // 类名.类方法(推荐) / 对象名.类方法(不推荐)
        Student.printHelloWorld();

        Student s = new Student();
        s.score = 61;
        s.printPass();
    }
}
