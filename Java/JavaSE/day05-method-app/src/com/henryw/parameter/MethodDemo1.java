package com.henryw.parameter;

/**
 * 进行了值传递，传输的是实参存储的值的副本
 */

public class MethodDemo1 {
    public static void main(String[] args) {
        int a = 10;
        change(a);
        System.out.println("main:" + a); // 10
    }

    public static void change(int a) {
        System.out.println("Change1: " + a); // 10
        a = 20;
        System.out.println("Change2: " + a); // 20
    }
}
