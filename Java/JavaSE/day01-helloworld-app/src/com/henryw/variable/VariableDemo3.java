package com.henryw.variable;

import org.w3c.dom.ls.LSOutput;

/**
 * 掌握基本数据类型的使用
 */

public class VariableDemo3 {
    public static void main(String[] args) {
        // 1. byte:占一个字节，即8位二进制，所以不可超出256个数（-128 ~ 127）
        byte a = 127;
        // byte a2 = 128 越界了

        // short：占两个字节
        short s = 13244;

        // int；占4个字节
        int i = 422424;

        // long：占8个字节
        // 注意：随便写一个整型自面量默认是int类型的，424242244444 虽然没有超过long的范围，但是超过了本身int类型的范围
        // 如果希望随便写一个整型自面量默认是long类型的，需要在后面加上L/l
        long lg = 424242244444L;

        // 2. float: 占四个字节
        // 注意：随便写小数字面量，默认是double，如果希望小数是float，后面加上F/f
        float f = 3.14F;

        // double: 占8个字节
        double d = 56.65;

        // 3. char: 字符型，字符类有且只能有一个
        char ch = 'a';
        char ch2 = '中';

        // 4. boolean
        boolean flag = true;
        boolean flag2 = false;

        // 拓展一种引用数据类型，后面要用，不是基础数据类型！
        // String称之为字符串类型，定义的变量可以用于记住一个字符串数据
        String name = "ZHANGSAN";
        System.out.println(name);
    }

}
