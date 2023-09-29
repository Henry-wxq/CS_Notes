package com.henryw.define;

/**
 * 解决业务需求不同时，使用不同的方法形式
 */

public class MethodDemo2 {
    public static void main(String[] args) {
        printHelloWorld1();

        System.out.println("-------------------------------------------------");

        printHelloWorld2(5);
    }

    // 无参数，无返回值方法
    // 如果方法不需要返回数据，返回值类型必须申明成void(无返回值申明)，此时方法内部不可以使用return返回数据
    public static void printHelloWorld1() {
        for (int i = 0; i < 3; i++) {
            System.out.println("Hello World");
        }
    }

    // 有参数，无返回值的方法
    public static void printHelloWorld2(int n) {
        for (int i = 0; i < n; i++) {
            System.out.println("Hello World");
        }
    }
}
