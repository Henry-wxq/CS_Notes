package com.henryw.extenddemo7;

/**
 * 通过this(...)调用兄弟构造器
 */

public class Test3 {
    public static void main(String[] args) {
        Student s1 = new Student("Henry", 20, "UOT");

        // 需求：如果学生没有填写学校，那么学校默认就是SCIE
        // 可以提供一个额外有参构造器
        Student s2 = new Student("Michelle", 20);
        System.out.println(s2.getName());
        System.out.println(s2.getAge());
        System.out.println(s2.getSchoolName());
    }
}

class Student{
    private String name;
    private int age;
    private String schoolName;

    public Student() {
    }

    public Student(String name, int age){
        this(name, age, "SCIE"); // 调用兄弟构造器
        // 不可以再一个构造器内既出现this()，又出现super()， 因为兄弟构造器中已经默认包含了super()，不能同时调用两次super()
        // 而且super()和this()都需要在第一行
    }

    public Student(String name, int age, String schoolName) {
        this.name = name;
        this.age = age;
        this.schoolName = schoolName;
    }

    public String getName() {
        return name;
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

    public String getSchoolName() {
        return schoolName;
    }

    public void setSchoolName(String schoolName) {
        this.schoolName = schoolName;
    }
}
