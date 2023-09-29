package com.henryw.parameter;

/**
 * 引用类型的值传递，发生了alias，相当于是实参把地址值拷贝了一份给形参，所以当方法内形参对这个地址内存储的数字进行改变以后，实参也会改
 */

public class MethodDemo2 {
    public static void main(String[] args) {
        int[] arr = {10, 15, 17};
        change(arr);
        System.out.println("main: " + arr[2]); // 1000
    }

    public static void change(int[] arr){
        System.out.println("Change1: " + arr[2]); // 17
        arr[2] = 1000;
        System.out.println("Change2: " + arr[2]); // 1000
    }
}
