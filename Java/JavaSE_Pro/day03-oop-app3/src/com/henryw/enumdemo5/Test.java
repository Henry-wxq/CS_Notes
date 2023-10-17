package com.henryw.enumdemo5;

/**
 * 枚举
 * 枚举类的第一行只能罗列一些名称，这些名称都是常量，并且每个常量记住的都是枚举类的一个对象
 * 枚举类的构造其都是私有的(写不写都只能是私有的)，因为枚举类对外不能创建对象
 * 每局都是最终类，不可以被继承
 * 枚举类中，从第二行开始，可以定义类的其它各种成员
 * 编译器为枚举类新增了及格方法，并且枚举类都是继承: java.lang.Enum类的，从enum类一会继承到一些方法
 */

public class Test {
    public static void main(String[] args) {
        A a1 = A.X;
        System.out.println(a1); // X
        // 可以使用cmd进行反编译，再对应的explorer中打开文件夹，javap A.class

        // 枚举类对外不能创建对象
        // A a = new A();

        // 枚举类的第一行都是常量，记住的是枚举类的对象
        A a2 = A.Y;

        // 枚举类提供一些个额外的API
        A[] as = A.values(); // 拿到全部对象
        A a3 = A.valueOf("Z");
        System.out.println(a3.name()); // Z
        System.out.println(a3.ordinal()); // 索引
    }
}
