package com.henryw.type;

/**
 * 表达式的自动类型转换机制
 * 表达式的最终结果类型由表达式中的最高类型决定
 */
public class TypeConversionDemo2 {
    public static void main(String[] args) {
        byte a = 10;
        int b = 20;
        long c = 30;
        char d = 'b';
        long rs = a + b + c + d;
        System.out.println(rs);

        // 在表达式中，byte，short，char是直接转换成int类型参与运算的
        byte i = 10;
        short j = 30;
        char k = 'c';
        int rs2 = i + j + k;
        System.out.println(rs2);
    }
}
