package com.henryw.polymorphismdemo2;

/**
 * 使用多态的好处
 * 在多态形式下，右边对象是解耦合的，便于扩展和维护
 *
 * 多态下不能使用子类的独有功能，因为编译时看左边，父类没有独有功能
 */

public class Test {
    public static void main(String[] args) {
        // 好处1：可以实现解耦合，右边对象可以随时切换，后续业务随即改变
        People p1 = new Teacher();
        p1.run(); // 后面代码无需更改
        // p1.test(); 编译时父类没有此独有方法，需要多态下的类型转换

        // 好处2：可以使用父类类型的变量作为形参，可以接收一切子类对象
        Student s = new Student();
        go(s);

        Teacher t= new Teacher();
        go(t);

    }


    public static void go(People p){

    }
}
