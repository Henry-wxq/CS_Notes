package com.henryw.collectiondemo1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

/**
 * Collection的常用方法：因为是单列集合的根接口，所以这些方法都是单列集合的通用方法
 */

public class Test2 {
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>(); // Collection是接口，不能实例化，所以这里用ArrayList实例化

        // boolean add(E e)：添加元素, 返回值表示是否添加成功, arrayList的add方法一定会返回true，因为可以重复
        c.add("hello");
        c.add("world");
        c.add("java");
        c.add("hello");
        System.out.println(c); // [hello, world, java, hello]

        // void clear()：清空集合中的所有元素
        c.clear();
        System.out.println(c); // []

        // boolean isEmpty()：判断集合是否为空, 如果为空返回true, 不为空返回false
        System.out.println(c.isEmpty()); // true

        // int size()：获取集合中的元素个数
        System.out.println(c.size()); // 0

        // boolean contains(Object o)：判断集合中是否包含指定的元素, 包含返回true, 不包含返回false
        c.add("hello");
        c.add("world");
        c.add("java");
        System.out.println(c.contains("hello")); // true
        System.out.println(c.contains("javaee")); // false

        // boolean remove(Object o)：删除集合中的指定元素, 返回值表示是否删除成功, 如果有重复元素，只会删除第一个
        c.add("hello");
        c.add("world");
        c.add("java"); // [hello, world, java, hello, world, java]
        System.out.println(c.remove("hello")); // true // [world, java, hello, world, java]

        // Object[] toArray()：将集合转换成数组
        Object[] objects = c.toArray(); // 泛型在运行的时候会被擦除，所以这里返回的是Object类型的数组
        System.out.println(Arrays.toString(objects)); // [world, java, hello, world, java]

        // 非要转换成String类型的数组，可以这样写
        String[] strings = c.toArray(new String[c.size()]);
        System.out.println(Arrays.toString(strings)); // [world, java, hello, world, java]

        System.out.println("----------------------------------");
        // 把一个集合的全部数据倒入到另一个集合中， Collection接口中没有索引，所以只能用这种方式， 相当于拷贝一份
        Collection<String> c2 = new ArrayList<>();
        c2.add("hello1");
        c2.add("world1");
        c2.add("java1");

        Collection<String> c3 = new ArrayList<>();
        c3.add("hello2");
        c3.add("world2");
        c3.add("java2");

        c2.addAll(c3); // 把c3的全部数据倒入到c2中，数据类型必须一致
        System.out.println(c2); // [hello1, world1, java1, hello2, world2, java2]
        System.out.println(c3); // c3不变，[hello2, world2, java2]，相当于拷贝
    }
}
