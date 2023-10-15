package com.henryw.extenddemo1;

/**
 * 继承的特点：
 * 1. 子类能继承父类的非私有成员(成员变量，成员方法)，即直接使用
 *
 * 继承后对象的创建：
 * 1. 子类的对象是由子类、父类共同完成的
 */

public class Test {
    public static void main(String[] args) {
        B b = new B(); // 此时B对象由两个设计图做出来的
        System.out.println(b.i);
    }
}
