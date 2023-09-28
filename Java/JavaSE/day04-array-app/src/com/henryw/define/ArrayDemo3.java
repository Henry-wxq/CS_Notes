package com.henryw.define;

/**
 * 遍历数组：求和，元素搜索，找最大值，最小值
 */

public class ArrayDemo3 {
    public static void main(String[] args) {
        int[] age_array = {12, 24, 36};

        // 快速书写数组遍历：直接敲：age_array.fori 即可
        for (int i = 0; i < age_array.length; i++) {
            System.out.println(age_array[i]);
        }

        // 计算某部门员工的销售总额，分别为5w，10w，26w，57w，100w
        int[] sold_array = {5, 10, 26, 57, 100};

        int sum = 0;
        for (int i = 0; i < sold_array.length; i++) {
            sum += sold_array[i];
        }
        System.out.println(sum);
    }

}
