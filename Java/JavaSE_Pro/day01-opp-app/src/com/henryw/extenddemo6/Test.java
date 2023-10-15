package com.henryw.extenddemo6;

/**
 * 子类中访问其它成员的特点：就近原则
 *
 * super指定访问当前类的父类，不是爷类
 */

public class Test {
    public static void main(String[] args) {
        B b = new B();
        b.showName();
        b.showMethod();
    }
}
