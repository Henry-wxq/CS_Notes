package com.henryw.collectiondemo2;

import java.util.ArrayList;
import java.util.Collection;

/**
 * 增强for循环: 用来遍历数组和集合的
 * for(元素类型 变量名 : 数组或者集合对象) {
 *    // 循环体
 *    // 变量就是元素
 *    // 数组或者集合对象就是容器
 * }
 *
 */

public class Test2 {
    public static void main(String[] args) {
        Collection<String> c = new ArrayList<>(); // Collection是接口，不能实例化，所以这里用ArrayList实例化
        c.add("Henry");
        c.add("William");
        c.add("Chloe");
        c.add("Maggie"); // [Henry, William, Chloe, Maggie]

        // 使用增强for循环遍历集合
        // 快速书写：c.for
        for (String ele : c) {
            System.out.println(ele); // Henry William Chloe Maggie
        }

        // 使用增强for循环遍历数组
        String[] arr = {"Henry", "William", "Chloe", "Maggie"};
        for (String ele : arr) {
            System.out.println(ele); // Henry William Chloe Maggie
        }
    }
}
