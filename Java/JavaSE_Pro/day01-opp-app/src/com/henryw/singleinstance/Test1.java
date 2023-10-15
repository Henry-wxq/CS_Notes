package com.henryw.singleinstance;

/**
 * 1. 设计模式：一个问题通常有多种解法，其中肯定有一种解法是最优的，这个最优的解法被人总结出来了，称之为设计模式；
 *      1) 设计模式共有20多种，对应20多种软件开发中会遇到的问题
 *      2) 设计模式主要学：解决什么问题？怎么写？
 * 2. 单例设计模式：确保一个类，只有一个对象
 *      1) 把类的构造器私有：外部不可创建A类的对象，于是只可以通过类的方法来创建
 *      2) 定义一个类变量记住类的一个对象
 *      3) 定义一个类方法，返回对象
 *
 */

public class Test1 {
    public static void main(String[] args) {
        A a1 = A.getObject();
        A a2 = A.getObject();
        System.out.println(a1);
        System.out.println(a2); // 地址一样
    }
}
