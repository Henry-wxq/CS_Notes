package com.henryw.extenddemo5;

import java.util.ArrayList;

/**
 * 常见应用场景：子类重写Object类的toString()方法，以便返回对象的内容
 * 输出对象时更想看到对象的内容，而不是内存地址
 */

public class Test {
    public static void main(String[] args) {
        Student s = new Student("Henry", 20);
//        System.out.println(s.toString());
        System.out.println(s); // 输出对象的时候会默认调用toString()方法，不重写会输出地址

        System.out.println("-----------------------------");

        ArrayList<String> list = new ArrayList<>();
        list.add("java");
        System.out.println(list); // 会输出内容而不是内存地址，说明Arraylist中重写了toString()方法
    }
}
