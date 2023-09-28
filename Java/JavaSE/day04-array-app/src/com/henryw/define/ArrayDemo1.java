package com.henryw.define;

/**
 * 静态初始化数组：定义数组的时候直接给数组赋值
 *
 * 格式：
 * 数据类型[] 数组名字 = new 数据类型[]{元素一，元素二，...}
 *
 * 简化格式：
 * 数据类型[] 数字名字 = {元素一，元素二，...}
 *
 * 注意：
 * “数据类型[] 数组名字” 也可以写成 “数据类型 数组名字[]”
 * 什么类型的数组只能存放什么类型的数据
 */

public class ArrayDemo1 {
    public static void main(String[] args) {
        // 完整
        int[] age_array = new int[]{19, 20, 25, 23, 21, 18}; // 是一个数组类型的变量
        double[] grade_array = new double[]{95, 88.5, 86.5, 80.5};
        System.out.println(age_array); // [I@e9e54c2
        /*
            [: 数组地址
            I: Int类型
            @: 在哪个地址
            后面的: 十六进制的地址信息
         */
        System.out.println(grade_array); // [D@65ab7765

        // 简化
        String[] name_array = {"Henry", "Chloe", "Maria"};
    }
}
