package com.henryw.stringbuilderdemo4;

public class Test2 {
    public static void main(String[] args) {
        // 目标：掌握StringBuilder的好处
        // 需求：拼接100万次abc
        // 先用String
//        String rs = "";
//        for (int i = 0; i < 1000000; i++) {
//            rs += "abc";
//        }
//        System.out.println(rs);

        // 使用StringBuilder，会快很多
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1000000; i++) {
            sb.append("abc");
        }
        System.out.println(sb);
    }
}
