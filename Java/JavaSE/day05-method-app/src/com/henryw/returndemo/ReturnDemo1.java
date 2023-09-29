package com.henryw.returndemo;

/**
 * 单独使用return;
 * 在无返回值方法中的作用：跳出并立即结束当前方法的执行
 */

public class ReturnDemo1 {
    public static void main(String[] args) {
        System.out.println("程序开始");
        chu(10, 0);
        System.out.println("程序结束");
    }

    public static void chu(int a, int b) {
        if (b == 0) {
            System.out.println("您的数据有问题，不能除0");
            return;
        }

        int c = a / b;
        System.out.println("除法结果是" + c);
    }
}
