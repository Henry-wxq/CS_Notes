package com.henryw.scanner;
// 1. 导包：一般不需要我们自己做，idea工具会帮助我们导包的
import java.util.Scanner;

/**
 * 使用Scanner接收用户键盘输入的数据
 */

public class ScannerDemo1 {
    public static void main(String[] args) {
        // 2. 得到一个键盘扫描器对象
        Scanner sc = new Scanner(System.in);

        // 3. 开始调用sc的功能，来接收用户键盘输入的数据
        System.out.println("请输入您的年龄： ");
        int age = sc.nextInt(); // 执行到这里，会开始等待用户输入一个整数，直到用户按了回车键，才会拿到数据
        System.out.println("您的年龄是：" + age);

        System.out.println("请输入您的名字： ");
        String name = sc.next(); // 开始等待用户输入一个字符串，直到用户按了回车键
        System.out.println(name + "，欢迎您进入系统！");

    }
}
