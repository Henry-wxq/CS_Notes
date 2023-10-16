package com.henryw.abstractdemo2;

/**
 * 抽象类的好处：更好的支持多态
 */

public class Test {
    public static void main(String[] args) {
        Animal a = new Cat();
        a.setName("叮当猫");
        a.cry(); // 更好的支持了多态
    }
}
