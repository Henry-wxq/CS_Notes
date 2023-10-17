package com.henryw.overload;

/**
 * 方法重载：一个类中，出现多个方法的名称相同，但是那它们的形参列表是不同的，么这些方法就成为方法重载了，不会起冲突
 *
 * 一个类中，只要名称一样，形参列表不同，那么就是方法重载了，如修饰符，返回值类型是否一样都无所谓
 * 形参列表不同，指的是：形参的个数，类型，顺序不同，不关心形参的名称
 */
public class MethodOverloadDemo1 {
    public static void main(String[] args) {
        test();
        test(100);
    }

    public static void test() {
        System.out.println("===test1===");
    }

    public static void test(int a) {
        System.out.println("===test2===" + a);
    }
}
