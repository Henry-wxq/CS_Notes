package com.henryw.variable;
/**
 * Java程序中支持书写二进制，八进制，十六进制的数据，分别需要以0B或者0b，0，0X或者0x开头
 */

public class ASCIIDemo1 {
    public static void main(String[] args) {
        // 二进制
        int a1 = 0B01100001;
        System.out.println(a1);

        // 八进制
        // 二进制换算八进制，每三位一个单元，计算即可
        int a2 = 0141;
        System.out.println(a2);

        // 十六进制
        // 二进制换算十六进制，每四位一个单元，计算即可
        // 10~15用A到F表示
        int a3 = 0XFA;
        System.out.println(a3);
    }
}
