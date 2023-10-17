package com.henryw.block;

/**
 * 代码块
 * 1. 静态代码块
 *      1) 格式: static{}
 *      2) 特点：类加载时自动执行，由于类只会加载一次，所以静态代码块也只会执行一次
 *      3) 作用：完成类的初始化，例如，对变量的初始化赋值
 * 2. 实例代码块
 *      1) 格式：{}
 *      2) 特点：每次创建对象时，执行示例代码块，并在构造器前执行
 *      3) 作用：和构造器一样，都是用来完成对象的初始化的，例如：对实例变量进行初始化赋值
 *      4) 可以用于做创建对象时的日志，减少构造器中写日志的重复代码，因为有参构造器可以有多个
 */

public class Student {
    static int number = 80;
    static String schoolName;

    static {
        System.out.println("静态代码块执行了");
        schoolName = "UOT";
    }

    {
        System.out.println("实例代码块执行了");
    }

    public Student(){
        System.out.println("无参数构造器执行了");
    }

    public Student(String name){
        System.out.println("有参数构造器执行了");
    }


}
