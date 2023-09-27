package com.henryw.loop;

/**
 * for循环的执行流程：
 * 1. 首先会执行初始化语句：int i = 0
 * 2. i = 0, 判断循环条件, 返回true, 计算机会进入到循环中执行输出第一行Hello World, 接着执行迭代语句i++
 * 3. i = 1, 判断循环条件, 返回true, 计算机会进入到循环中执行输出第二行Hello World, 接着执行迭代语句i++
 * 4. i = 2, 判断循环条件, 返回true, 计算机会进入到循环中执行输出第三行Hello World, 接着执行迭代语句i++
 * 5. i = 3, 判断循环条件，返回false, 循环就会立即结束
 */

public class ForDemo1 {
    public static void main(String[] args) {
        // 需求：打印多行Hello World

        for (int i = 0; i < 5; i++) {
            System.out.println("Hello World");
        }

    }
}
