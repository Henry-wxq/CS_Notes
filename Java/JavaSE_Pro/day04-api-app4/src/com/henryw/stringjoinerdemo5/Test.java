package com.henryw.stringjoinerdemo5;

import java.util.StringJoiner;

/**
 * StringJoiner是JDK8开始才有的，跟StringBuilder一样，也是用来操作字符串的，也可以堪称是一个容器，创建之后里面的内容是可变的
 * 好处：不仅能提高字符串的操作效率，并且再有些长囧下使用它操作字符串，代码会更简洁
 *
 * 构造器
 * 1. 创建一个对象，指定拼接是的间隔符号
 *      public StringJoiner(间隔符号)
 * 2. 船舰一个对象，指定拼接是的间隔符号，开始符号，结束符号
 *      public StringJoiner(间隔符号，开始符号，结束符号)
 *
 * 常用方法
 * 1. 添加数据，并返回对象本身
 *      public StringJoiner add(添加的内容)
 * 2. 返回长度(字符出现的个数)
 *      public int length()
 * 3. 返回一个字符串(该字符串就是拼接之后的结果)
 *      public String toString()
 */

public class Test {
    public static void main(String[] args) {
        StringJoiner s1 = new StringJoiner(", ");
        s1.add("Java1");
        s1.add("Java2");
        s1.add("Java3");
        System.out.println(s1);

        StringJoiner s2 = new StringJoiner(", ", "[", "]");
        s2.add("Java1");
        s2.add("Java2");
        s2.add("Java3");
        System.out.println(s2);

        System.out.println("-------------------------------------------------------------------");

        System.out.println(getArrayData(new int[]{11, 22, 33}));
    }

    public static String getArrayData(int[] arr){
        // 1. 判断arr是否为null
        if (arr == null) {
            return null;
        }

        // 2. arr数组对象存在。arr = [11, 22, 33]
        StringJoiner s = new StringJoiner(", ", "[", "]");
        for (int i = 0; i < arr.length; i++) {
            s.add(arr[i] + "");
        }

        return s.toString();
    }
}
