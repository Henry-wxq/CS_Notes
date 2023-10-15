package com.henryw.polymorphismdemo2;

public class Teacher extends People {
    public String name = "Teacher";

    @Override
    public void run() {
        System.out.println("老师跑的贼慢");
    }


    public void teach(){
        System.out.println("老师需要教学");
    }
}
