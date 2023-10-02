package com.henryw.arraylist;

import java.util.ArrayList;

/**
 * ArrayList
 */

public class ArrayListDemo1 {
    public static void main(String[] args) {
        // 1. 创建一个ArrayList的集合对象
        // 打上尖括号约束集合内的数据类型
        // ArrayList<String> list = new ArrayList<String>();
        // 从jdk 1.7开始支持
        ArrayList<String> list = new ArrayList<>(); // 最为标准，后面不用再明确写了

        // 2. 将指定元素添加到此集合的末尾，成功则返回true
        list.add("Henryw");
        list.add("Henryw"); // 可以重复添加
        System.out.println(list); // 不会打印地址，会直接打印结果

        System.out.println("-----------------------------------------");

        // 3. 往集合中的某个索引位置处添加一个数据
        list.add(1, "Chloey");
        System.out.println(list);

        System.out.println("------------------------------------------");

        // 4. 获取集合中某个索引位置处的元素值
        String rs1 = list.get(1);
        System.out.println(rs1);

        System.out.println("-------------------------------------------");

        // 5. 返回集合中的元素个数(集合大小)
        System.out.println(list.size());

        System.out.println("--------------------------------------------");

        // 6. 根据索引删除集合中某个索引位置的元素值，返回被删除的元素值
        System.out.println(list.remove(1));
        System.out.println(list);

        System.out.println("---------------------------------------------");

        // 7. 直接删除指定元素值，删除成功返回true
        System.out.println(list.remove("Henryw")); // 若有重复值，只会默认删除第一次出现的数据
        System.out.println(list);

        System.out.println("---------------------------------------------");

        // 8. 修改某个索引位置处的数据，修改后会返回原来的值给我们
        System.out.println(list.set(0, "Mariam"));
        System.out.println(list);
    }
}
