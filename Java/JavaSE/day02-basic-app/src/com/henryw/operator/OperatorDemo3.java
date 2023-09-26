package com.henryw.operator;

/**
 * 掌握扩展赋值运算符的使用
 * 内含了强制类型转换，强制转换成a的类型
 */

public class OperatorDemo3 {
    public static void main(String[] args) {
        // a += b; a = (a's type) a + b
        int a = 10;
        double b = 2.0;
        System.out.println(a += b);

        // a -= b;
        // a *= b;
        // a /= b;
        // a %= b;

        System.out.println("-----------------------------------------");

        byte x = 13;
        byte y = 12;
        // 编译报错
        // x = x + y;
        x += y; // x = (byte) (x + y)
        System.out.println(x);


    }
}
