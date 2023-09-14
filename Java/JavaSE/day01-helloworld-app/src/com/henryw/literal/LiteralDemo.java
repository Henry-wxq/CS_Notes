package com.henryw.literal;

public class LiteralDemo {
    public static void main(String[] args) {
        // 目标：掌握常见数据在程序中的书写格式
        // 1. 整数
        System.out.println(666);

        // 2. 小数
        System.out.println(99.5);

        // 3. 字符：必须用单引号围起来，有且只能有一个字符
        System.out.println('0');
        System.out.println(' '); // 空字符
        // 错误字符
        // System.out.println('  ');
        // System.out.println('两个');
        // 特殊字符： \m 换行; \t tab
        System.out.println('中');
        System.out.println('\n');
        System.out.println('国');

    }
}
