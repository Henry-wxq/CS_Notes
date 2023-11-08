package com.henryw.genericdemo8;

import com.henryw.enumdemo5.A;

import java.util.ArrayList;

public class Test {
    public static void main(String[] args) {
        // MyArrayList list = new MyArrayList(); // 若不使用泛型，则均为Object类型
        MyArrayList<String> list = new MyArrayList<>(); // 把String类型送到E里面
        list.add("Java1");
        list.add("Java2");
        String element = list.get(1);
        System.out.println(element);

        MyClass<String, MyArrayList<String>> c2 = new MyClass<>();

        MyClass2<Cat> c3 = new MyClass2<>(); // 不能送String，因为没有继承Animals，用来限定类型变量
        MyClass2<Animals> c4 = new MyClass2<>();
    }
}
