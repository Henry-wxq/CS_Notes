package com.henryw.innerclassdemo3;

/**
 * 使用场景
 * 可以更方便的创建出一个子类对象
 * 匿名内部类通常作为参数传输给方法
 */

public class Test2 {
    public static void main(String[] args) {
        Swimming dog = new Swimming(){
            @Override
            public void swim(){
                System.out.println("狗游泳飞快");
            }
        };

        go(dog);
    }

    // 设计一个方法，可以接收swimming接口的一切实现类对象进来参加游泳比赛
    public static void go(Swimming s){
        System.out.println("开始");
        s.swim();
    }
}

// 猫和狗都要参加游泳比赛
interface Swimming{
    void swim();
}
