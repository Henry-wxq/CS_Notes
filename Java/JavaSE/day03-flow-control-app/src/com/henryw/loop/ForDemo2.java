package com.henryw.loop;

// for loop 批量产生数据

public class ForDemo2 {
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            System.out.println(i);
        }

        System.out.println("-----------------------------------------------");

        // 1到100奇数的和
        // 方法一
        int sum_1 = 0;
        for (int i = 1; i <= 100; i+=2) {
            sum_1 += i;
        }
        System.out.println(sum_1);

        // 方法二
        int sum_2 = 0;
        for (int i = 0; i <= 100; i++) {
            if (i % 2 == 1) {
                sum_2 += i;
            }
        }
        System.out.println(sum_2);

    }
}
