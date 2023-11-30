package com.henryw.collectiondemo1;

import java.util.ArrayList;
import java.util.HashSet;

/**
 * 集合体系结构
 * 1. Collection  单列集合的根接口: 每一个元素只能存储一个对象（一个值）
 * 2. Map         双列集合的根接口：每一个元素包含两个对象（两个值， 键值对）
 *
 * Collection<E>集合体系结构: 接口，实现类
 * 1. List<E>接口：元素有序，元素可重复，有索引
 *  - ArrayList<E>：底层数据结构是数组，查询快，增删慢
 *  - LinkedList<E>：底层数据结构是链表，查询慢，增删快
 * 2. Set<E>接口：元素无序，元素不可重复, 没有索引
 *  - HashSet<E>：底层数据结构是哈希表，线程不安全，可以存储null值, 无序
 *      - LinkedHashSet<E>：底层数据结构是哈希表+链表，线程不安全，可以存储null值， 有序
 *  - TreeSet<E>：底层数据结构是红黑树（二叉树），按照大小默认升序排序，线程不安全，不可以存储null值
 */

public class Test1 {
    public static void main(String[] args) {
        // 简单确认一下collection集合的特点
        ArrayList<String> list = new ArrayList<>(); // 有序，可重复，有索引
        list.add("hello");
        list.add("world");
        list.add("java");
        System.out.println(list); // [hello, world, java]

        HashSet<String> set = new HashSet<>(); // 无序，不可重复，没有索引
        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("hello");
        System.out.println(set); // [world, java, hello], 加进去的顺序和打印出来的顺序不一致，但是，加进去以后顺序就不会变了
    }
}
