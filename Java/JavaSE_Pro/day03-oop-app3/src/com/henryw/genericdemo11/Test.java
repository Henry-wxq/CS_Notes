package com.henryw.genericdemo11;

import java.util.ArrayList;

public class Test {
    public static void main(String[] args) {
        // 1. 泛型是工作在编译阶段的，一旦程序编译成class文件，class文件中就不存在泛型了，这就是泛型擦除(此处在out中的Test.class中)
        ArrayList<String> list = new ArrayList<>();
        list.add("Java1");
        list.add("Java2");
        String rs = list.get(1);
        System.out.println(rs);

        // 2. 泛型不支持基本数据类型，只能支持对象类型(引用数据类型)
        // ArrayList<int> list1 = new ArrayList<>();
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Double> list2 = new ArrayList<>();
    }
}
