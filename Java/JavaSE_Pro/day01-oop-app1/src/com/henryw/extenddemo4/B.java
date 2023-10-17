package com.henryw.extenddemo4;

public class B extends A{
    // 方法重写
    @Override // 使用注解
    public void print1(){
        System.out.println("2");
    }

    // 注意，参数列表也需一样
    @Override
    public void print2(int a, int b){
        System.out.println("1" + (a - b));
    }
}
