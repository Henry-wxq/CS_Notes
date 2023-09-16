package com.henryw.variable;

/**
 * 1. 变量就是内存中的一块儿区域，可以理解成一个盒子，用来装一个数据
 */

public class VariableDemo1 {
    public static void main(String[] args) {
        // 1. 定义一个整数变量
        // 数据类型 变量名 = 数据
        // 注意： =在Java中是赋值的意思，从右往左看
        int age = 12;
        System.out.println(age);

        // 2. 小数类型：double
        double score = 99.5;
        System.out.println(score);

        System.out.println("------------------------------");

        // 3. 使用变量的好处:便于扩展和维护
        // 在改动数据的时候可以通过改变变量完成数据的快速改变
        // e.g. 666改成888
        int number = 888;
        System.out.println(number);
        System.out.println(number);
        System.out.println(number);

        System.out.println("------------------------------");

        // 4. 变量的特点：里面装的数据可以被替换
        int age2 = 18;
        System.out.println(age2);
        age2 = 19; // 赋值：从右边往左边执行
        System.out.println(age2);
    }
}
