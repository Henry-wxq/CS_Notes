package com.henryw.finaldemo1;

/**
 * 常量
 * 使用类static final修饰的成员变量被成为常量
 *
 * 作用
 * 通常用与记录系统的配置信息
 *
 * 优势
 * 代码可读性更好，可维护性更好
 * 程序编译后，常量会被‘宏替换’：出现常量的地方全部会被替换成其记住的自变量，这样可以保证使用常量和直接用字面量的性能是一样的
 */

public class Test2 {
    public static final String SCHOOL_NAME = "UOT";

    public static void main(String[] args) {
        System.out.println(SCHOOL_NAME);
    }
}
