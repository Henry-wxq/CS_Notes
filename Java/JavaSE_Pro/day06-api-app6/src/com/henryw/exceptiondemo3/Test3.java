package com.henryw.exceptiondemo3;

import java.util.Scanner;

/**
 * 捕获异常，尝试重新修复
 */

public class Test3 {
    public static void main(String[] args) {
        // 需求：调用一个方法，让用户输入一个合适的价格返回为止
        while (true) {
            try {
                System.out.println(getMoney());
                break;
            } catch (Exception e) {
                System.out.println("请您输入合法数字");;
            }
        }
    }

    public static double getMoney(){
//        while (true) {
//            Scanner sc = new Scanner(System.in);
//            System.out.println("请您输入合适的价格: ");
//            double money = sc.nextDouble();
//            if (money >= 0) {
//                return money;
//            } else {
//                System.out.println("您输入的价格是不合适的"); // 需要重新输入一遍，Ctrl + alt + t，第三个死循环
//            }
//        } // 看起来好像没问题，但是如果输入的不是一个double类型的，那么会报错，程序直接崩，所以可以在最上层捕获异常，让用户重新输入，直到成功为止

        while (true) {
            Scanner sc = new Scanner(System.in);
            System.out.println("请您输入合适的价格: ");
            double money = sc.nextDouble();
            if (money >= 0) {
                return money;
            } else {
                System.out.println("您输入的价格是不合适的"); // 需要重新输入一遍，Ctrl + alt + t，第三个
            }
        }
    }
}
