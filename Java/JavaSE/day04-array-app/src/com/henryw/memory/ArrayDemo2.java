package com.henryw.memory;

/**
 * 多个变量指向同一个数组对象的形式
 */
public class ArrayDemo2 {
    public static void main(String[] args) {
        int[] arr1 = {10, 15, 18};
        int[] arr2 = arr1; // 直接把arr1中的地址传给arr2，相当于产生了alias，因为他们指向同一个堆内存中的地址
        System.out.println(arr1);
        System.out.println(arr2);

        arr2[1] = 99;
        System.out.println(arr1[1]); // 验证alias

        // 如果某个数组储存的值是null，那么它将不储存任何的堆内存地址
        arr2 = null;
        System.out.println(arr2); // 不会出问题
        System.out.println(arr2[1]); // 不可以访问其中的数据 NullPointerException
    }
}
