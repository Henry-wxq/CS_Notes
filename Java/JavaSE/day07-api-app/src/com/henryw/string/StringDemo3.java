package com.henryw.string;

/**
 * String注意事项
 */

public class StringDemo3 {
    public static void main(String[] args) {
        // 1. String的对象是不可变的
        // 若更改字符串对象，其实是在堆内存中创建一个新的字符串，然后将栈内存中main方法下的name变量指向新的字符串对象
        String name = "Henry";
        String name2 = "Michelle";
        name += name2;
        System.out.println(name);

        // 2. 只要是以双引号方式写出的字符串变量，会存储到字符串常量池，且相同内容的字符串只存储一份
        String s1 = "abc";
        String s2 = "abc";
        System.out.println(s1 == s2);

        // 3. 但通过new方式创建的字符串对象，每new一次都会产生一个新的对象放在堆内存中
        char[] chars = {'a', 'b', 'c'};
        String c1 = new String(chars);
        String c2 = new String(chars);
        System.out.println(c1 == c2);

        // 4. 题目，假设每道题都在一个新的文档中
        // 1
        String s3 = new String("abc"); //  产生了两个对象，"abc"是字符串对象，放在常量池中；new出来的字符串放在堆内存中
        String s4 = "abc"; //  创建了0个对象，因为常量池中已经有"abc"了
        System.out.println(s3 == s4); // false， 因为一个指向的是常量池中的，一个指向的是new出来的

        // 2
        String s5 = "abc"; // 放在常量池
        String s6 = "ab";
        String s7 = s6 + "c"; // 只要是进行了运算，都在堆内存中进行
        System.out.println(s5 == s7); // false

        // 3
        String s8 = "abc";
        String s9 = "a" + "b" + "c"; // 因为这一行会运用java的编译优化机制，java在编译时，会直接转成"abc"
        System.out.println(s8 == s9); // true


    }
}
