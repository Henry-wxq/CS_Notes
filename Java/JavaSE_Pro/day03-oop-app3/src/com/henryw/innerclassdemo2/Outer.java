package com.henryw.innerclassdemo2;

public class Outer {
    private int age;
    public static String schoolName; // 静态方法可以直接访问静态成员变量，不能直接访问实例成员变量，因为是属于每个成员的，静态内部类同理

    // 静态内部类
    public static class Inner{
        private String name;
        public static int a;

        public void test(){
            System.out.println(schoolName); // ok
            // System.out.println(age); // not ok，需要用外部类对象来访问
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public static int getA() {
            return a;
        }

        public static void setA(int a) {
            Inner.a = a;
        }
    }
}
