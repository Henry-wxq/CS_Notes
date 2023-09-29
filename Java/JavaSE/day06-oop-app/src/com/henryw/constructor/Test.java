package com.henryw.constructor;

public class Test {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "Chloe";
        s1.score = 85;
        System.out.println(s1.name);
        System.out.println(s1.score);


        Student s2 = new Student("Maria", 100);
        System.out.println(s2.name);
        System.out.println(s2.score);
    }
}
