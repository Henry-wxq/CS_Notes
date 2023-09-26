package com.henryw.operator;

/**
 * 掌握基本的算数运算符的使用
 */

public class OperatorDemo1 {
    public static void main(String[] args) {
        int a = 10;
        int b = 2;
        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b); // 5
        System.out.println(a % b); // 取余

        int i = 5;
        int j = 5;
        System.out.println(i / j); // 两个整数相除还是整数，向下取整
        System.out.println(1.0 * i / j); // 一定要小数，则在前面乘一个1.0

        // ‘+’与字符串运算的时候是用作连接符的，其结果依然是一个字符串
        // 有‘+’，能算就算，不能算的在一起
        int a2 = 5;
        System.out.println("abc" + a2); // "abc5"
        System.out.println(a2 + 5); // 10
        System.out.println("henry" + 5 + 'v'); // "henry5v"
        System.out.println(a2 + 'a' + "henryw"); // “102henryw” 前面能算，后面不能算，从左往右
    }
}
