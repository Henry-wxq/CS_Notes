package com.henryw.demo;

/**
 * 完成数组反转
 */

public class Test1 {
    public static void main(String[] args) {
        // 1. 准备一个数组
        int[] arr = {10, 20, 30, 40, 50};

        // 2. 定义一个循环，这集两个变量，一个在前一个灾后
        // 注意此时","的使用
        for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
            // arr[i] arr[j]
            // 1. 创建一个临时变量，储存最后的值
            int temp = arr[j];

            // 2. 将前面的值赋给后面
            arr[j] = arr[i];

            // 3. 将临时变量的值赋给前面
            arr[i] = temp;
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
