package com.henryw.polymorphismdemo1;

/**
 * 多态
 * 1. 对象多态
 * 2. 行为多态：都是人的行为，在不同对象下表现出不同特征
 *
 * 前提
 * 1. 有继承/实现关系
 * 2. 存在父类引用子类对象
 * 3. 存在方法重写
 *
 * 注意
 * Java中的成成员变量不存在多态性，该咋样就咋样
 */

public class Test {
    public static void main(String[] args) {
        // 1. 对象多态
        People p1 = new Teacher(); // 小范围给大范围
        p1.run(); // 识别技巧：编译看左边，运行看右边，即编译时，看的时是People中有没有run，运行时时运行的Teacher中的run

        People p2 = new Student();
        p2.run(); // 识别技巧：编译看左边，运行看右边

        // 变量没有多态性，编译是谁，运行就是谁
        System.out.println(p1.name); // People
        System.out.println(p2.name); // People
    }
}
