package com.henryw.operator;

/**
 * 三元运算符
 * 格式：条件表达式 ？ 值1：值2
 * 执行流程：首先计算关系表达式的值，如果值为true，返回值1，如果为false，返回值2
 * 应用场景：90 成绩及格！ 25 成绩不及格！
 */

public class OperatorDemo6 {
    public static void main(String[] args) {
        double score = 98.5;
        String rs = score >= 60 ? "成绩及格" : "成绩不及格";
        System.out.println(rs);

        double score2 = 59.5;
        String rs2 = score2 >= 60 ? "成绩及格" : "成绩不及格";
        System.out.println(rs2);

        // 需求一：找出两个整数中的较大值，并输出
        int a = 99;
        int b = 67;
        int max = a > b ? a : b; // 两个数相等亦可以
        System.out.println(max);

        // 需求二：找出三个整数中的较大值，并输出
        int i = 10;
        int j = 20;
        int k = 34;
        int temp = i > j ? i : j;
        int max2 = k > temp ? k : temp;
        System.out.println(max2);
    }
}
