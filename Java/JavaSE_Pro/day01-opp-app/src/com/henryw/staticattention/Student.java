package com.henryw.staticattention;



public class Student {
    static String schoolName; // 类变量
    double score; // 实例变量

    // 1. 类方法中可以直接访问类的成员，不可以直接访问实例成员
    public static void printHelloWorld(){
        // 同一个类中，访问类成员，可以省略类名不写
        Student.schoolName = "UOT"; // 可以直接访问
        Student.printHelloWorld2(); // 可以直接用printHelloWorld2();

        // 不可以直接访问实例成员
//        System.out.println(score); // 实例变量
//        printPass(); // 实例方法

        // 不可以出现this, 因为找不到对象
//        System.out.println(this);
    }

    // 类方法
    public static void printHelloWorld2(){
        System.out.println(schoolName);
    }

    // 2. 实例方法中既可以直接访问类成员，也可以直接访问实例成员
    // 实例方法
    public void printPass(){
        // 可以直接访问类成员，并进行更改，此时，所有对象共享此一个新赋值的类变量
        schoolName = "UOT2";
        printHelloWorld2();

        // 可以直接访问实例成员
        System.out.println(score);
        printPass2(); // 相当于前面有个this，当调对象的时候，也会调调printPass，和此对象下的printPass2

        // 可以出现this关键字
        this.printPass2();
    }

    public void printPass2(){

    }
}


