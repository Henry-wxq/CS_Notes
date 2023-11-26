package com.henryw.systemdemo2;

/**
 * System代表程序所在的系统，也是一个工具类
 *
 * System类提供的常见方法
 * 1. 终止当前运行的Java虚拟机: public static void exit(int status)
 * 2. 返回当前系统的时间毫秒值的形式: public static long currentTimeMillis()
 */

public class Test {
    public static void main(String[] args) {
        // 1. public static void exit(int status)
        // status 参数用作状态代码；按照惯例，非零状态代码表示异常终止
        // System.exit(0); // 人为终止虚拟机，程序在虚拟机中跑，相当于后续程序全部挂掉，不要使用，相当于删库跑路
        System.out.println("-----------------------------");

        // 2. public static long currentTimeMillis()
        // 获取当前系统的时间
        // 返回的是long类型的时间毫秒值，指的是从1970-1-1 0:0:0开始走到此刻的总的毫秒值；1s = 1000ms
        // 用来做代码的性能分析
        long time1 = System.currentTimeMillis();
        System.out.println(time1);

        for (int i = 0; i < 1000000; i++) {
            System.out.println("输出了:" + i);
        }

        long time2 = System.currentTimeMillis();
        System.out.println((time2 - time1) / 1000.0 + "s");

    }
}
