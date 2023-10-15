package com.henryw.polymorphismdemo1;

public class Teacher extends People{
    public String name = "Teacher";

    @Override
    public void run() {
        System.out.println("老师跑的贼慢");
    }
}
