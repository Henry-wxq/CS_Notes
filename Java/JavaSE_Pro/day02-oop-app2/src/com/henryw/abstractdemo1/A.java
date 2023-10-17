package com.henryw.abstractdemo1;

// 抽象类
public abstract class A {
    private String name;
    public static String schoolName;

    public A(){

    }

    public A(String name){
        this.name = name;
    }

    // 抽象方法只有方法签名，没有方法体
    public abstract void run();
}
