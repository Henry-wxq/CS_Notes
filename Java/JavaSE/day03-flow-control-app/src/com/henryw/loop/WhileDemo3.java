package com.henryw.loop;

/**
 * 1. while循环的书写格式：
 *      初始化语句;
 *      while (循环条件) {
 *          循环体语句(被重复执行的代码);
 *          迭代语句;
 *      }
 *
 * 2. 知道循环几次用for，不知道循环几次建议使用while
 */

public class WhileDemo3 {
    public static void main(String[] args) {
        // 打印多行Hello World
        int i = 0;
        while (i <= 5) {
            System.out.println("Hello World");
            i ++;
        }

    }
}
