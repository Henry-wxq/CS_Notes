package com.henryw.mapdemo1;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

/**
 * Map集合成为双列集合
 * 1. 格式：{key1=value1, key2=value2, key3=value3, ...}，一次存储一对数据作为一个元素，不允许重复的key，可以有重复的value
 * 2. Map集合的每个元素成为一个Entry对象，Entry对象包含key和value，Entry对象是一个键值对对象，Map集合也称为键值对集合
 *
 * 应用场景
 * 1. 用于存储具有映射关系的数据，如：学号和学生信息，身份证号和人员信息，手机号和联系人信息等
 *
 * Map集合体系
 * Map<K, V>接口 (K: key的类型，V: value的类型)
 * - HashMap<K, V>实现类：底层是哈希表，查询速度快，线程不安全，效率高，允许null键和null值
 * -- LinkedHashMap<K, V>实现类：底层是哈希表+链表，查询速度快，线程不安全，效率高，允许null键和null值，有序集合
 * - TreeMap<K, V>实现类：底层是红黑树，查询速度慢，线程不安全，效率高，不允许null键，允许null值，有序集合
 *
 * Map集合体系的特点： Map系列集合的特点都是由键决定的，与值无关
 * - HashMap：无序，不重复，无索引，键和值可以为null（用的最多）
 * - LinkedHashMap：有序，不重复，无索引，键和值可以为null
 * - TreeMap：有序（按照键的大小默认升序排序），不重复，无索引，键不可以为null，值可以为null
 *
 */

public class Test {
    public static void main(String[] args) {
//        Map<String, Integer> map = new HashMap<>(); // 经典代码。 按照键，无序，不重复，无索引，键和值可以为null
        Map<String, Integer> map = new LinkedHashMap<>(); // 经典代码。 按照键，有序，不重复，无索引，键和值可以为null
        map.put("a", 1);
        map.put("b", 2);
        map.put("c", 4);
        map.put("c", 3); // key重复，value覆盖
        map.put(null, null);
        System.out.println(map); // {null=null, a=1, b=2, c=3} // {a=1, b=2, c=3, null=null}

        Map<Integer, String> map1 = new TreeMap<>(); // 可排序，不重复，无索引，键不可以为null，值可以为null
        map1.put(1, "a");
        map1.put(3, "c");
        map1.put(2, "b");
        map1.put(2, "d"); // key重复，value覆盖
        System.out.println(map1); // {1=a, 2=d, 3=c}
    }
}
