package com.henryw.demo;

import java.util.Random;
import java.util.Scanner;

/**
 * 某公司开发部5名开发人员，要进行项目进展汇报演讲，先在采取随机排名后进行汇报。请先一次录入5名员工的工号，然后展示出一组随机的排名顺序
 */

public class Test2 {
    public static void main(String[] args) {
        // 使用动态初始化
        int[] arr = new int[5];

        Random index = new Random();
        Scanner mans = new Scanner(System.in);

        // 录入5名员工的工号
        for (int i = 0; i < arr.length; i++) {
            System.out.println("第" + (i + 1) + "位员工的工号是： ");
            int man_num = mans.nextInt();
            arr[i] = man_num;
        }

        // 依次遍历数组中的每个数据
        for (int i = 0; i < arr.length; i++) {
            // 每遍历到一个数据，都随机一个索引值出来，让当前数据与该所以位置处的数据进行交换
            int temp_index = index.nextInt(arr.length);

            int temp_man = arr[temp_index];

            arr[temp_index] = arr[i];
            arr[i] = temp_man;
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

    }
}
