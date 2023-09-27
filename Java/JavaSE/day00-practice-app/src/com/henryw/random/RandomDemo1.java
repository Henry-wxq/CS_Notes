package com.henryw.random;

import java.util.Random;

/**
 *
 */

public class RandomDemo1 {
    public static void main(String[] args) {
        // 1. 导包：不用自己写，IDEA会生成

        // 2. 创建一个Random对象，用于生成随机数
        Random r1 = new Random();

        // 3. 调用Random提供的功能：nextInt得到随机数
        int data = r1.nextInt(10); // 包前不包后：0到9中的数随机生成
        System.out.println(data); // 若是觉得不够，选中两行代码，Ctrl + Alt + t, 可以快速添加成为loop

//        for (int i = 1; i <= 5; i++) {
//            int data2 = r1.nextInt(10);
//            System.out.println(data2);
//        }

        System.out.println("--------------------------------------------------------------");

        // 4. Random生成指定区间的随机数：减加法，在后面加数字即可
        // 1 ~ 10 -> -1 -> (0 ~ 9) + 1
        for (int i = 1; i <= 20; i++) {
            int data2 = r1.nextInt(10) + 1;
            System.out.println(data2);
        }
    }
}
