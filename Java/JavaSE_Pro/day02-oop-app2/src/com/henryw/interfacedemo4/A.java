package com.henryw.interfacedemo4;

/**
 * 因为接口的方法是要供别人使用的，所以默认是public
 */

public interface A {
    // 1. 默认方法：必须使用default修饰，默认会被public修饰，不用写public
    //      实例方法：对象的方法，必须使用实现类的对象来访问
    default void test1(){
        System.out.println("--默认方法--");
        test2();
    }

    // 2. 私有方法：必须使用private修饰(JDK9开始才支持)
    //      实例方法：对象的方法，但是实现类不能直接调用，因为是私有的
    private void test2(){
        System.out.println("--私有方法--");
    }

    // 3. 静态方法：vixu使用static修饰
    //      属于类本身拥有的方法，需要用接口来调用
    static void test3(){
        System.out.println("--静态方法--");
    }
}
