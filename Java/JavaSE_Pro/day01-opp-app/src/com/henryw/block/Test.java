package com.henryw.block;

/**
 *
 */

public class Test {
    public static void main(String[] args) {
        System.out.println(Student.number);
        System.out.println(Student.schoolName); // 也说明静态代码块只执行一次

        System.out.println("-------------------------------------------------");

        Student s1 = new Student();
        Student s2 = new Student("Henry"); // 每次创建对象都会执行实例代码块
    }
}
