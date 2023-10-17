package com.henryw.interfacedemo1;

/**
 * 接口
 * 1. 成员变量(默认为常量，需要赋值),前面可以不加public static final
 * 2. 成员方法(默认为抽象方法，不能写方法体)，前面可以不加public abstract
 * 3. 不能写构造器或者代码块
 * 4. 不能创建对象
 *
 * 接口是用来被类实现(implements)的，实现接口的类成为实现类
 * 一个类可以实现多个接口(接口可以理解成干爹)，实现类实现多个接口，必须重写完全部接口的全部抽象方法，否则类需要定义成抽象类
 */

public class Test {
    public static void main(String[] args) {
        System.out.println(A.SCHOOL_NAME);

        D d = new D();
    }
}
