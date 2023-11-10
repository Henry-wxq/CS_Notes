package com.henryw.objectdemo1;

import java.util.Objects;

// Cloneable是一个标记接口，是一种规则
public class Student implements Cloneable{
    private String name;
    private int age;

    public Student() {
    }

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    // 输入toS回车即可重写
    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    // 重写equals代码，比较两个对象的内容一样就返回true
    // 输入eq不断回车即可
    @Override
    public boolean equals(Object o) {
        // 判断两个对象是否地址一样，一样直接返回true
        if (this == o) return true;
        // 判断o是null，就直接返回false，或者比较者的类型与被比较者的类型不一样，返回false
        if (o == null || this.getClass() != o.getClass()) return false;
        // o不是null，且o一定是学生类型的对象，开始比较内容了
        Student student = (Student) o;
        return this.age == student.age && Objects.equals(this.name, student.name);
    }

    // clone是protected的，只能在子类或者父类中调用，不能在子类对象中调用，所以s1对象不能直接调用
    // 需要cloneable标记
    @Override
    protected Object clone() throws CloneNotSupportedException {
        // super去调用父类Object中的clone方法
        return super.clone();

        // 深克隆
        // User u2 = (User) super.clone();
        // u2.数组 = u2.数组.clone();
        // return u2;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
