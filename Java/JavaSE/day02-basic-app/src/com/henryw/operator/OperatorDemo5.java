package com.henryw.operator;

import org.w3c.dom.ls.LSOutput;

/**
 * 逻辑运算符
 * &: 逻辑与, 两边都是true才返回true，左右都要执行
 * |: 逻辑或, 两边只要有一边是true就返回true，左右都要执行
 * !: 逻辑非
 * ^: 逻辑异或，先后结果相同时返回false，不同时返回true
 * &&: 双与，左边为false，右边不执行
 * ||: 双或，左边为true，右边不执行
 */

public class OperatorDemo5 {
    public static void main(String[] args) {
        int storage = 8;
        double size = 6.5;

        // &
        boolean rs = size >= 6.5 & storage >= 8;
        System.out.println(rs);

        // |
        boolean rs2 = size >= 6.5 | storage >= 16;
        System.out.println(rs2);

        // !
        System.out.println(!true);

        boolean rs3 = !(storage >= 16);
        System.out.println(rs3);

        // ^
        System.out.println(true ^ true); // false
        System.out.println(true ^ false); // true

        // &&
        int i = 10;
        int j = 20;
        System.out.println(i > 100 && ++j > 99);
        System.out.println(j);
        System.out.println(i > 100 & ++j > 99);
        System.out.println(j);

        // ||
        int m = 10;
        int n = 30;
        System.out.println(m > 3 || ++n > 40);
        System.out.println(n);
        System.out.println(m > 3 | ++n > 40);
        System.out.println(n);
    }

}
