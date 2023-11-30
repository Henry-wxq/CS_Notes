package com.henryw.collectiondemo2;


import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

/**
 * Collection的遍历方法
 * 1. 迭代器: 是用来遍历集合的专用方式(数组没有迭代器)，
 * 2. 增强for循环，没有索引，所以不能用普通for，因为Collection接口继承了Iterable接口，所以可以使用增强for循环
 * 3. lambda表达式
 *
 * Collection的迭代器
 * - 迭代器是一个接口，无法直接使用，需要使用Collection接口中的iterator()方法获取迭代器的实现类对象，在java中迭代器的代表是Iterator接口
 *
 * Collection集合获取迭代器的方法：
 * - Iterator<E> iterator()：返回集合中的迭代器对象，该迭代器对象默认指向当前集合中的第一个元素
 *
 * 迭代器的常用方法：
 * - boolean hasNext()：询问集合中是否还有下一个元素，如果有就返回true，没有就返回false
 * - E next()：获取当前指向的元素，并且让迭代器指向下一个元素
 */

public class Test1 {
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>(); // Collection是接口，不能实例化，所以这里用ArrayList实例化
        c.add("Henry");
        c.add("William");
        c.add("Chloe");
        c.add("Maggie"); // [Henry, William, Chloe, Maggie]

        // 使用迭代器遍历集合
        // 1. 从集合对象中获取迭代器对象：使用集合中的iterator()方法获取迭代器的实现类对象，使用Iterator接口接收(多态)
        Iterator<String> it = c.iterator(); // 站在第一个元素处，即Henry处
//        System.out.println(it.next()); // Henry
//        System.out.println(it.next()); // William
//        System.out.println(it.next()); // Chloe
//        System.out.println(it.next()); // Maggie // 到这里已经没有下一个元素了，所以下面的代码会报错
//        System.out.println(it.next()); // java.util.NoSuchElementException

        // 2. 使用while循环遍历
        while (it.hasNext()) { // 判断是否还有下一个元素
            String ele = it.next(); // 获取下一个元素
            System.out.println(ele); // Henry William Chloe Maggie
        }
    }
}
