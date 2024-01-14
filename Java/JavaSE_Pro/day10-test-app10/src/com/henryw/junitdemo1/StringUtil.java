package com.henryw.junitdemo1;

/**
 * 字符串工具类
 */

public class StringUtil {
    public static void printNumber(String name) {
        if (name == null) {
            System.out.println("名字不能为null");
            return; // 结束方法
        }
        System.out.println("名字长度是: " + name.length());
    }

    /*
    求字符串的最大索引
     */
    public static int getMaxIndex(String str) {
        if (str == null) {
            return -1;
        }
        return str.length() - 1;
        }
}
