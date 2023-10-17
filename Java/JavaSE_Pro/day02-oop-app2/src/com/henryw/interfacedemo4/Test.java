package com.henryw.interfacedemo4;

/**
 * 从JDK8开始新出现的三种新的带方法体的方法，不用再重写了，增强了接口的能力，也便于项目的维护
 */

public class Test {
    public static void main(String[] args) {
        B b = new B();
        b.test1();

        A.test3();
    }
}
