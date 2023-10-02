package com.henryw.staticdemo11;

/**
 * 有无static修饰成员变量
 */

public class Student {
    // 类变量：有static修饰，属于类，在计算机里只有一份，会被类的全部对象共享；即，一旦赋了值，所有的对象访问的类变量都是同一个
    static String name;

    // 实例变量(成员变量; 对象变量)：无static修饰，属于每个对象的
    int age;
}
