package com.henryw.innerclassdemo1;

public class Outer {
    private int age = 99;
    public static String a;

    // 成员内部类
    public class Inner{
        private String name;
        public static String schoolName; // JDK16开始才支持定义静态成员
        private int age = 88;

        public void test(){
            // 内部类属于外部类的一个成员，可以访问其外部类成员
            System.out.println(age);
            System.out.println(a);

            int age = 66;
            System.out.println(age); // 66 (最近)
            System.out.println(this.age); // 88 (内部类对象)
            System.out.println(Outer.this.age); // 99 (成员方法中通过外部类.this访问其外部类对象)
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public static String getA() {
        return a;
    }

    public static void setA(String a) {
        Outer.a = a;
    }
}
