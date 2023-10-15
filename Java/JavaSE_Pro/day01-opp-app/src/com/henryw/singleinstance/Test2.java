package com.henryw.singleinstance;

/**
 * 懒汉式单例设计：那对象时，才开始创建
 *
 * 懒汉式和饿汉式的选择：当单例对象被频繁使用，应该用饿汉式；如果不是很频繁，那么就用懒汉式
 */

public class Test2 {
    public static void main(String[] args) {
        B b1 = B.getInstance(); // 第一次拿对象
        B b2 = B.getInstance();
        System.out.println(b1 == b2);
    }
}
