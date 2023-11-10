package com.henryw.objectdemo1;

/**
 * Object类中的常见方法
 * 1. 返回对象的字符串表示形式
 *      public String toString
 * 2. 判断两个对象是否相等(默认比较两个对象的地址)
 *      public boolean equals(Object o)
 * 3. 对象克隆
 *      protected Object clone() (浅克隆)
 *
 * 浅克隆：拷贝出的担心对象，与原对象中的数据一模一样(引用类型拷贝的只是地址，比如数组只会拷贝地址，不会创建新的数组)
 * 深克隆：对象中基本类型的数据直接拷贝，对象中的字符串数据拷贝的还是地址，对象中还包含的其它对象，不会拷贝地址，会创建新对象
 */

public class Test {
    public static void main(String[] args) throws CloneNotSupportedException {
        Student s1 = new Student("Henry", 20);

        // System.out.println(s1.toString()); // 输出对象默认调用
        System.out.println(s1); // 不更改的话会返回地址，所以Object中toString存在目的是为了重写此方法, 输入toS回车即可重写

        Student s2 = new Student("Henry", 20);
        System.out.println(s2.equals(s1)); // 默认比较两个对象的地址，因为又==存在，所以Object中equals存在目的是为了重写此方法
        System.out.println(s2 == s1); // 默认比较两个的地址

        Student s3 = (Student) s1.clone();
        System.out.println(s3.getName());
        System.out.println(s3.getAge());
        System.out.println(s1 == s3); // false
    }
}
