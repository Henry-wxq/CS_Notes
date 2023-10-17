package com.henryw.polymorphismdemo2;

public class Student extends People {
    public String name = "Student";

    @Override
    public void run() {
        System.out.println("学生跑的贼快");
    }

    public void exam(){
        System.out.println("学生需要考试");
    }
}
