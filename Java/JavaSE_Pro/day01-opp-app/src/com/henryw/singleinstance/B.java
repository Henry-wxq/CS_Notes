package com.henryw.singleinstance;

public class B {
    // 2. 定义一个类变量，用于存储这个类的变量(先不要写出来)
    private static B b;

    // 1. 把类的构造器私有
    private B(){

    }

    // 3. 定义一个类方法，保证第一次调用时才创建对象，后面调用时都会用这一个对象返回
    public static B getInstance(){
        if (b == null){
            System.out.println("第一次创建对象");
            b = new B();
        }
        return b;
    }
}
