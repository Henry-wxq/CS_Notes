package com.henryw.type;

/**
 * 自动类型转换：类型范围小的变量，可以直接赋值给类型范围大的变量
 * byte -> short -> int -> long -> float -> double
 * char -> int -> long -> float -> double
 */

public class TypeConversionDemo1 {
    public static void main(String[] args) {
        byte a = 12;
        int b = a; // 发生了自动类型转换
        System.out.println(a);
        System.out.println(b);

        // char -> float
        // 'a' 97 => 00000000 01100001
        char c = 'a';
        float d = c;
        System.out.println(d);
    }
}
