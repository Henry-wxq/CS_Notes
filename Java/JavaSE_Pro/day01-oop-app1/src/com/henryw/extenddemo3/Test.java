package com.henryw.extenddemo3;

/**
 * Java是单继承的：一个类中只能继承一个直接父类；java中的类不支持多继承，但是支持多层继承
 * Object类是java中所有类的祖宗，我们写的任何一个类，都是Object类的子类或者子孙类，可以调用Object类的方法
 */

public class Test {
    public static void main(String[] args) {
        A a = new A();
        // a.可以看到很多方法，都是Object的方法
    }
}

class A{} // 相当于是class A extends Object{}

class B extends A{} // B间接是Object类的子孙类

class C extends B{}

// class D extends B, C{} 不支持多继承
