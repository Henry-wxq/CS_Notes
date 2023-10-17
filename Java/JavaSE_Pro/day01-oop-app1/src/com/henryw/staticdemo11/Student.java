package com.henryw.staticdemo11;

/**
 * 有无static修饰成员变量
 *
 * 类变量的应用场景：在开发中，如果某个数据只需要一份，且希望能够被共享(访问，修改)，则该数据可以定义成类变量来记住
 * e.g. 系统启动后，要求用户类可以记住自己创建了多少个用户对象了:
 * public class User{
 *     // 类变量
 *     public static int number;
 *
 *     // 构造器
 *     public User{
 *         User.number++; // 可以直接写number++, 因为在同一个类中访问自己的类变量，可以省略类名不写
 *     }
 * }
 */

public class Student {
    // 类变量：有static修饰，属于类，在计算机里只有一份，会被类的全部对象共享；即，一旦赋了值，所有的对象访问的类变量都是同一个
    static String name;

    // 实例变量(成员变量; 对象变量)：无static修饰，属于每个对象的
    int age;
}
