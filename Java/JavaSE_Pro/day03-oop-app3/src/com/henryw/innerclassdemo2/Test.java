package com.henryw.innerclassdemo2;

/**
 * 静态内部类：有static修饰的内部类，属于外部类自己持有
 */

public class Test {
    public static void main(String[] args) {
        // 访问静态内部类
        Outer.Inner in = new Outer.Inner(); // 不需要先创建外部类对象

    }
}
