package com.henryw.javabean;

public class Test {
    public static void main(String[] args) {
        // 存储一个学生的数据
        Student s1 = new Student();
        s1.setName("Chloe");
        s1.setScore(99);
        System.out.println(s1.getName());
        System.out.println(s1.getScore());
    }
}
