package com.henryw.loop;

/**
 * 书写格式：
 *      do {
 *          循环体语句;
 *          迭代语句;
 *      } while (循环条件);
 *
 * 特点:先执行，后判断
 *
 * 应用场景：抢票，先刷新，再判断是否没票
 */

public class DoWhileDemo5 {
    public static void main(String[] args) {
        // 打印多行Hello World
        int i = 0;
        do {
            System.out.println("Hello World");
            i++;
        } while (i < 3);
    }
}
