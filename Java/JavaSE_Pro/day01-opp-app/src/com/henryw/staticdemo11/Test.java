package com.henryw.staticdemo11;



public class Test {
    public static void main(String[] args) { // 先把mian方法加载到栈内存
        // 1. 类变量的用法
        // 类名.类变量(推荐)
        Student.name = "Henryw"; // 把Test.class和Student.class加载到方法区(包括其中的方法和变量), 并同时在堆内存中创建类变量
        // 类变量开始为null，后变成Henryw

        // 对象.类变量(不推荐)
        Student s1 = new Student();  // 栈内存中产生Student s1对象，储存堆内存中的age变量的地址，堆内存中age变量一开始为0，
        // age变量还存储了方法区中Student.class的地址
        s1.name = "Mariam"; // 不推荐此方法； 找到堆内存中的类变量，并改为Mariam

        // 2. 类变量的特点，计算机中只有一份
        Student s2 = new Student();
        s2.name = "Michellew";

        System.out.println(s1.name); // Michellew
        System.out.println(Student.name); // Michellew

        // 3. 实例变量的用法：属于每个对象
        // 对象.实例对象 (不可通过类名访问，因为属于对象)
        s1.age = 23;
        s2.age = 18;
        System.out.println(s1.age); // 23
    }
}
