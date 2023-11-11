package com.henryw.stringbuilderdemo4;

/**
 * StringBuilder代表可变字符串对象，相当于是一个容器，它里面装的字符串都是可以改变的，就是用来操作字符串的
 * 好处：StringBuilder比String更是和做字符串的修改操作，效率会更高，代码也会更简洁
 *
 * 构造器：
 * 1. 空白
 *      public StringBuilder()
 * 2. 指定字符串
 *      public StringBuilder(String str)
 *
 * 常用方法：
 * 1. 添加数据并返回StringBuilder对象本身
 *      public StringBuilder append(任意类型)
 * 2. 将对象内容反转
 *      public StringBuilder reverse()
 * 3. 返回对象内容长度
 *      public int length()
 * 4. 通过toString()就可以实现把StringBuilder转换为String
 *      public String toString()
 *
 * 谁调用方法，this就是谁
 */

public class Test1 {
    public static void main(String[] args) {
        StringBuilder s1 = new StringBuilder(); // s ""
        StringBuilder s2 = new StringBuilder("Henry"); // s "Henry"

        // 1. 拼接内容
        s1.append(12);
        s1.append("Maria");
        s1.append(true);

        // 支持链式编程
        s2.append(666).append("Chloe").append(false);

        System.out.println(s1); // 12Mariatrue  不是地址说明重写了toStirng方法
        System.out.println(s2); // Henry666Chloefalse

        // 2. 反转操作
        s2.reverse();
        System.out.println(s2);

        // 3. 返回字符串的长度
        System.out.println(s1.length());

        // 4. 把StringBuilder的对象转换成String
        String rs1 = s1.toString();
        System.out.println(rs1);
    }
}
