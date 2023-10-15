package com.henryw.extenddemo1;

// 子类
public class B extends A{
    // 子类是可以直接使用父类的非私有成员
    public void print3(){
        System.out.println(i);
    }
}
