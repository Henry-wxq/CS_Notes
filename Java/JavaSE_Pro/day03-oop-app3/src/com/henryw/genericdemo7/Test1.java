package com.henryw.genericdemo7;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class Test1 {
    public static void main(String[] args) {
        // 没有使用泛型
        ArrayList list = new ArrayList();
        list.add("java1");
        list.add("java2");
        list.add("java3");
        list.add(new Cat()); // 没有使用泛型的时候可以往里面添加一切类型的数据

        for (int i = 0; i < list.size(); i++) {
            // String e = list.get(i); // 不可以，需要强制转换
            String e = (String) list.get(i);
            System.out.println(e); // 猫对象报错

        }
    }
}

class Cat{}

