package com.henryw.objectsdemo2;

import java.util.Objects;

/**
 * Objects类是一个工具类，提供了很多静态方法
 * 1. 先做非空判断，再比较两个对象(使用这个而不使用其自己的equals方法的原因：调用对象为null，报错，NullPointerException)
 *      public static boolean equals(Object a, Object b)
 * 2，判断对象是否为null，为null返回true，反之false(可以使用==替代)：
 *      public static boolean isNull(Object obj)
 * 3. 判断对象是否部位null，为null则返还true，反之
 *      public static boolean nonNull(Object obj)
 */

public class Test {
    public static void main(String[] args) {
        String s1 = null;
        String s2 = "Henry";

        // System.out.println(s1.equals(s2)); // NullPointerException
        System.out.println(Objects.equals(s1, s2)); // false

        System.out.println(Objects.isNull(s1)); // true
        System.out.println(s1 == null);
        System.out.println(Objects.isNull(s2)); // false
    }
}
