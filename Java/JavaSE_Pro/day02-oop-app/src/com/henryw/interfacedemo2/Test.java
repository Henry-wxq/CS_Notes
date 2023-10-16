package com.henryw.interfacedemo2;

/**
 * 使用接口的好处：
 * 1. 弥补了类单继承的不足，一个类同时可以实现多个接口
 * 2. 让程序可以面向接口编程，这样程序员就可以灵活方便的切换各种业务实现
 */

public class Test {
    public static void main(String[] args) {
        Student s = new Student();
        // Driver s = new A();
        // Singer s = new A();
    }
}

class A extends Student implements Driver, Singer{
    @Override
    public void drive() {

    }

    @Override
    public void sing() {

    }
}

class Student{}

interface Driver{
    void drive();
}

interface Singer{
    void sing();
}
