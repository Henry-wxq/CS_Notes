package com.henryw.literal;

import org.w3c.dom.ls.LSOutput;

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
        // 特殊字符： \n 换行; \t tab
        System.out.println('中');
        System.out.println('\n');
        System.out.println('国');

        // 4. 字符串：必须用双引号围起来，里面的内容可以随意
        System.out.println("         ");

        // 5. 布尔值：只有两个值 true false
        System.out.println(true);
        System.out.println(false);

    }
}
