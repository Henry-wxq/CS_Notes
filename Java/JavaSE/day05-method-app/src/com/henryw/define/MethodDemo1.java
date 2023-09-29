package com.henryw.define;

/**
 * 方法：一种语法架构，它可以把一段代码封装成一个功能，以便重复调用
 *
 * 格式：
 * 修饰符 返回值类型 方法名(形参列表){
 *     方法体代码(需要执行的功能代码)
 *     return 返回值
 * }
 */

public class MethodDemo1 {
    // 现在很多的程序员都要进行两个整数求和操作
    public static int sum(int a, int b) {
        int c = a + b;
        return c;
    }

    public static void main(String[] args) {
        int rs1 = sum(10, 20);
        System.out.println(rs1);
    }
}
