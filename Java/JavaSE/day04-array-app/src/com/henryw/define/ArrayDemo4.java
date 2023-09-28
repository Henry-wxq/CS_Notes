package com.henryw.define;

/**
 * 数组的动态初始化格式（不可与静态初始化混用）: 常应用于开始不确定具体元素值，只知道元素个数的场景
 * 数据类型[] 数组名字 = new 数据类型[长度]
 *
 * 后赋值
 * arr[0] = 10
 *
 * 动态初始化元素默认值：
 * byte, shot, char, int, long: 0
 * float, double: 0
 * boolean: false
 * 类，接口，数组，String: null
 */

public class ArrayDemo4 {
    public static void main(String[] args) {
        int[] ages = new int[3]; // ages = [0, 0, 0] 默认值
        for (int i = 0; i < ages.length; i++) {
            System.out.println(ages[i]);
        }

        // 对其赋值
        int[] ages_num = {10, 13, 18};
        for (int i = 0; i < ages.length; i++) {
            ages[i] = ages_num[i];
            System.out.println(ages[i]);
        }
    }
}
