package com.henryw.collectiondemo2;

import java.util.ArrayList;
import java.util.Collection;
import java.util.function.Consumer;

/**
 * Lambda表达式: JDK8开始的新技术, 用来遍历map集合很好用
 * 1. Lambda表达式是一个匿名函数，将函数作为一个方法的参数进行传递
 *
 * 需要使用collection的如下方法来完成, 继承的是Iterable接口的方法
 * - default void forEach(Consumer<? super E> action)：对此集合的每个元素执行操作
 */

public class Test3 {
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>(); // Collection是接口，不能实例化，所以这里用ArrayList实例化
        c.add("Henry");
        c.add("William");
        c.add("Chloe");
        c.add("Maggie"); // [Henry, William, Chloe, Maggie]

        // 使用Lambda表达式遍历集合
//        c.forEach(new Consumer<String>() {
//            @Override
//            public void accept(String s) {
//                System.out.println(s);
//            }
//        });

//        c.forEach((String s) -> {
//                System.out.println(s);
//        });

//        c.forEach(s -> {
//                System.out.println(s);
//        });

//        c.forEach(s -> System.out.println(s) );

        c.forEach(System.out::println);
    }
}
