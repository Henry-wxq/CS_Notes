package com.henryw.lambdademo1;

/**
 * lambda表达式：JDK8开始支持的新特性
 * 作用：简化匿名内部类的写法
 *
 * 格式：
 * (被重写方法的形参列表) -> {
 *     被重写方法的方法体
 * }
 *
 * 注意：lambda表达式只能简化接口中只有一个抽象方法的接口的匿名内部类的写法，即函数式接口
 * 和将来见到的大部分函数时接口，上面都可能会有一个注解：@FunctionalInterface
 *
 */

public class Test1 {
    public static void main(String[] args) {
        // 匿名内部类，是Animal的子类对象
//        Animal a = new Animal() {
//            @Override
//            public void run() {
//                System.out.println("狗在跑");
//            }
//        };
//        a.run();

        // lambda表达式是有使用前提的，并不是说能简化全部匿名内部类的写法，只能简化函数式接口的匿名内部类的写法，即接口中只有一个抽象方法的接口
        // Animal不是接口，是一个错误示范
//        Animal a = () -> {
//            System.out.println("狗在跑");
//        };
//        a.run();

//        Swimming s1 = new Swimming() {
//            @Override
//            public void swim() {
//                System.out.println("学生在游泳");
//            }
//        };
//        s1.swim();

        // lambda表达式, 因为swim没有形参，所以使用()替代
        Swimming s2 = () -> {
            System.out.println("学生在游泳");
        };
        s2.swim();
    }
}

abstract class Animal {
    public abstract void run();
}

interface Swimming{
    void swim();
}
