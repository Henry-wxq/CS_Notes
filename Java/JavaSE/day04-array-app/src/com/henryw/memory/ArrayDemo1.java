package com.henryw.memory;

/**
 * Java程序在计算机中的执行过程
 *
 * Java内存分配介绍
 * 1. 方法区: 字节码文件加载的地方，把class文件提取到这里，包括main方法
 * 2. 栈: 方法运行时所进入的内存，变量也是在这里，e.g. main方法就是从方法区提取到这里运行的
 * 3. 堆: new出来的东西会在这块内存中开辟空间并产生地址
 * 4. 本地方法栈
 * 5. 寄存器
 */

public class ArrayDemo1 {
    public static void main(String[] args) { // 把ArrayDemo1和main提取到方法区，main随后被提取到栈内存
        int a = 10; // 在栈内存中储存
        System.out.println(a);

        int[] arr = {11, 22, 33}; // 在栈内存中创建arr，然后在堆内存中储存{11, 22, 33}，并把堆内存中的地址，赋值给栈内存的arr
        System.out.println(arr);

        arr[0] = 100; // 通过栈内存arr中的地址，找到堆内存中的0，然后改成100
    }
}
