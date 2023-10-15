package com.henryw.finaldemo1;

/**
 * final
 * 1. final修饰类，类不能被继承了; 又是用于工具类
 * 2. final修饰方法，方法不能被重写了
 * 3. final修饰变量总规则：有且仅能赋值一次；可以用来保护数据不被更改，如圆周率等
 *      1. 局部变量
 *      2. 成员变量
 *          1. 静态成员变量
 *          2. 实例成员变量：一般不用，因为直接把实例变量限制死了，没有意义
 *
 * 常量：public static final修饰的成员变量，建议名称全部大写，多个单词下划线链接
 *
 * 注意
 * final修饰基本类型的变量，变量存储的数据不能被改变
 * final修饰引用类型的变量，变量存储的地址不能被改变，但是地址所指向对象的内容是可以被改变的
 */

public class Test {
    public static final String School_Name = "UOT";

    public static void main(String[] args) {
        // 3. final修饰变量总规则：有且仅能赋值一次
        final int a;
        a = 12;
        // a = 13; // 属于第二次赋值，会报错

        final double r = 3.14; // 不希望别人去改

        // schoolName = "SCIE"; // 二次赋值，会报错

        // 修饰引用类型的变量
        final int[] arr = {1, 2, 3};
        // arr = null; // 不可改变地址
        arr[1] = 6; // 可以改变地址所指向对象的内容
    }

    // 保护值不被改动
    public static void but(double z){
        // z = 0.1; // 不可二次赋值，如果z的input是一个final修饰的变量的话，哪怕此时z是局部变量
    }
}

// 1. final修饰类，类不能被继承了; 又是用于工具类
final class A{}
//class B extends A{}

// 2. final修饰方法，方法不能被重写了
class C{
    public final void test(){

    }
}

class D extends C{
//    @Override
//    public void test(){
//
//    }
}
