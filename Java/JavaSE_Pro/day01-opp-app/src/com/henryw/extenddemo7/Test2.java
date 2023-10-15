package com.henryw.extenddemo7;

/**
 * 子类构造器为什么要调用父类构造器
 */

public class Test2 {
    public static void main(String[] args) {
        Teacher t = new Teacher();
    }
}

class Teacher extends People{
    private String skill;

    public String getSkill() {
        return skill;
    }

    public void setSkill(String skill) {
        this.skill = skill;
    }
}

class People{
    private String name;
    private int age;

    public People() {
    }

    public People(String name, int age) {
        this.name = name;
        this.age = age;
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
}
