package com.henryw.extenddemo6;

public class B extends A{
    String name = "Chloe";

    public void showName(){
        String name = "Michelle";
        System.out.println(name); // Michelle 局部变量
        System.out.println(this.name); // Chloe 子类成员变量
        System.out.println(super.name); // Henry 父类成员变量
    }

    @Override
    public void print(){
        System.out.println("--子类方法--");
    }

    public void showMethod(){
        print();
        super.print();
    }
}
