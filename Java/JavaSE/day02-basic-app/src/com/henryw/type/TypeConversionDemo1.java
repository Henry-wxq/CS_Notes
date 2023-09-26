package com.henryw.type;

/**
 * 自动类型转换：类型范围小的变量，可以直接赋值给类型范围大的变量
 */

public class TypeConversionDemo1 {
    public static void main(String[] args) {
        byte a = 12;
        int b = a; // 发生了自动类型转换
        System.out.println(a);
        System.out.println(b);
    }
}
