package com.henryw.type;

/**
 * 强行类型转换：强行将类型范围大的变量，数据赋值给类型范围小的变量
 * 数据类型 变量2 = (数据类型) 变量1
 */

public class TypeConversionDemo3 {
    public static void main(String[] args) {
        int a = 20;
        byte b = (byte) a; // ALT + ENTER 强制类型转换
        System.out.println(a);
        System.out.println(b);

        int i = 1500; // 00000101 11011100
        byte j = (byte) i; // 11011100 1代表结果是一个负数，二进制的第一位是符号位，0是正，1是负
        System.out.println(j); // 36

        double d = 99.5;
        int m = (int) d;
        System.out.println(m);  // 丢掉小数部分，保留整数部分
    }
}
