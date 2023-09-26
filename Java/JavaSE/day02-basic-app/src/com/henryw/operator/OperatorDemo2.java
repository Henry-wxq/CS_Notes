package com.henryw.operator;

import java.util.jar.JarOutputStream;

/**
 * 自增自减运算符：只能操作变量，不能操作字面量
 * 自增：++，对变量自身的值加一
 * 自减：--，对变量自身的值减一
 * 单独使用时放在变量前后都可以
 * 但是非单独使用会有区别
 */

public class OperatorDemo2 {
    public static void main(String[] args) {
        int a = 10;
        a++;
        System.out.println(a);
        ++a;
        System.out.println(a);

        a--;
        System.out.println(a);
        --a;
        System.out.println(a);

        System.out.println("----------------------------------------------");

        // 不是单独使用
        // 在前面：先加后用，即先对i加1，再把值赋给rs
        int i = 10;
        int rs = ++i;
        System.out.println(rs); // 11
        System.out.println(i); // 11

        // 在后面：先用后加，先把j的值赋给rs2，再对j自增
        int j = 10;
        int rs2 = j++;
        System.out.println(rs2); // 10
        System.out.println(j); // 11
    }
}
