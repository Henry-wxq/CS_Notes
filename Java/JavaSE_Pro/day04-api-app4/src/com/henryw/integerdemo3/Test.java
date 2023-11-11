package com.henryw.integerdemo3;

import java.util.ArrayList;

/**
 * 包装类：把基本数据类型包装成对象
 * 1. byte: Byte
 * 2. short: Short
 * 3. int: Integer
 * 4. long: Long
 * 5. char: Character
 * 6. float: Float
 * 7. double: Double
 * 8. boolean: Boolean
 *
 * 包装方案
 * 1. 使用构造器(已过时)
 *      public Integer(int value)
 * 2. 使用方法
 *      public static Integer valueOf(int i)
 *
 * 包装类的常见操作
 * 1. 把其它基本数据类型转换成字符串类型
 *      public static String to String()
 *      public String toString
 * 2. 可以把字符串类型的数值转换成数值本身对应的数据类型
 *      public static int parseInt(String s)
 *      public static Integer valueOf(String s)
 */

public class Test {
    public static void main(String[] args) {
        // Integer a1 = new Integer(12);
        Integer a2 = Integer.valueOf(12);
        System.out.println(a2);

        // 自动装箱：可以自动转换，不要弄我们去写代码
        Integer a3 = 12;

        // 自动拆箱：可以自动把包装类型的对象，转换成对应的基本数据类型
        int a4 = a3;

        // 泛型和集合不支持基本数据类型，只支持引用数据类型，即对象
        // ArrayList<int> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        list2.add(12); // 自动装箱
        int rs = list2.get(0); // 自动拆箱

        System.out.println("--------------------------------------------------------------------------------");

        // 1. 把基本类型的数据转换成字符串
        Integer a = 23;
        String s1 = Integer.toString(a);
        System.out.println(s1 + 1); // 231

        String s2 = a.toString(); // "23"
        System.out.println(s2 + 1); // 231

        String s3 = a + ""; // 23
        System.out.println(s3 + 1);

        // 2. 把字符串类型的数值转换成对应的基本类型
        String ageStr = "29";
        // int ageI = Integer.parseInt(ageStr); // 29
        int ageI = Integer.valueOf(ageStr); // 29 更好的方法，因为都一样
        System.out.println(ageI + 1); // 30

        String scoreStr = "99.5";
        double score = Double.valueOf(scoreStr); // 99.5
        System.out.println(score + 0.5); // 100.0
    }
}
