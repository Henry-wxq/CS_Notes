package com.henryw.overload;

/**
 *  方法重载的应用场景
 *  开发中我们经常需要为处理一类业务，提供多种解决方案，此时方法重载来设计是很专业的
 *
 *  优势
 *  1. 可读性高
 *  2. 可以在内部复用
 *
 *  开发武器系统，功能需求如下：
 *  1. 可以默认发一枚武器
 *  2. 可以指定地区发射一枚武器
 *  3. 可以指定地区发射多枚武器
 */

public class MethodOverloadDemo2 {
    public static void main(String[] args) {
        fire();
        fire("米国");
    }

    public static void fire() {
//        System.out.println("发射了一枚武器给岛国");
        fire("岛国"); // 内部复用
    }

    public static void fire(String country) {
//        System.out.println("发射了一枚武器给" + country);
        fire(country, 1);
    }

    public static void fire(String country, int number) {
        System.out.println("发射了" + number + "枚武器给" + country);
    }
}
