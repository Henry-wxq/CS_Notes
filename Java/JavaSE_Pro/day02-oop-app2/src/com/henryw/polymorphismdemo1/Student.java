package com.henryw.polymorphismdemo1;

public class Student extends People{
    public String name = "Student";

    @Override
    public void run() {
        System.out.println("学生跑的贼快");
    }
}
