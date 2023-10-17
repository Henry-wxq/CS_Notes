package com.henryw.innerclassdemo1;

/**
 * 内部类：
 * 如果一个类定义再另一个类的内部，这个类就是内部类
 * 当一个类的内部，包含了一个完整的事物，且这个事物没有必要单独设计时，就可以把这个事物设计成内部类
 *
 * 成员内部类：类中的一个普通成员，类似与之前普通的成员变量，成员方法
 */

public class Test {
    public static void main(String[] args) {
        // 访问成员内部类：外部类.内部类
        // 不可以直接new成员内部类的对象，因为依赖于外部类对象，需要先new外部类对象
        Outer.Inner in = new Outer().new Inner();

    }
}
