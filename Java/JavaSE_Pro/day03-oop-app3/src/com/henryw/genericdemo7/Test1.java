package com.henryw.genericdemo7;
import java.util.ArrayList;

/**
 * 泛型：定义类，接口，方法时，同时声明了一个或者多个类型变量(如：<E>)，称为泛型类，泛型接口，泛型方法，它们统称为泛型
 * e.g. public class ArrayList<E>{
 *
 *      }
 *
 * 作用：泛型提供了在编译阶段约束所能操作的数据类型，并自动进行检查的能力；可以避免强制类型转换，及其可能出现的异常
 * 本质：把具体的数据类型作为参数传给类型变量
 */

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

        System.out.println("-------------------------------------");
        // 使其只能加入String，约束能加入的类型
        ArrayList<String> list1 = new ArrayList<>(); // 从JDK1.7开始后面的尖括号中可以不用声明
        list1.add("Java1");
        // list.add(new Cat()); // 报错

        for (int i = 0; i < list.size(); i++) {
            String e = list1.get(i);
            System.out.println(e);
        }
    }
}

class Cat{}

