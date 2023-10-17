package com.henryw.innerclassdemo3;

/**
 * 匿名内部类
 * 一种特殊的局部内部类，所谓匿名，指的时程序员不需要为这个类声明名字
 *
 * 特点
 * 匿名内部类本质是一个子类，并会立即创建出一个子类对象
 *
 * 作用
 * 用于更方便的创建一个子类对象
 */

public class Test {
    public static void main(String[] args) {
//        Animal a = new Cat();
//        a.cry();

        // 匿名内部类
        // 1. 把这个匿名内部类编译成一个子类，然后会理解创建一个子类对象出来
        Animal a = new Animal(){
            @Override
            public void cry() {
                System.out.println("喵喵喵的叫");
            }
        };
        a.cry();
    }
}

//class Cat extends Animal{
//    @Override
//    public void cry(){
//        System.out.println("喵喵喵的叫");
//    }
//}

abstract class Animal{
    public abstract void cry();
}
