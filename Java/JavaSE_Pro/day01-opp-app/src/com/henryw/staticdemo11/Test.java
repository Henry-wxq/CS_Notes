package com.henryw.staticdemo11;



public class Test {
    public static void main(String[] args) {
        // 1. 类变量的用法
        // 类名.类变量(推荐)
        Student.name = "Henryw";

        // 对象.类变量(不推荐)
        Student s1 = new Student();
        s1.name = "Mariam"; // 不推荐

        // 2. 类变量的特点，计算机中只有一份
        Student s2 = new Student();
        s2.name = "Michelle";

        System.out.println(s1.name); // Michelle
    }
}
