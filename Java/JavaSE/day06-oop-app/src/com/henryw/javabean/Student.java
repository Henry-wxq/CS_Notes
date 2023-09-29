package com.henryw.javabean;

/**
 * 实体类：一种特殊形式的类，只用于保存数据
 * 1. 这个类中的成员变量都要私有，并且要对外提供相应的getXXX，setXXX方法
 * 自动生成方法：右键 - generate - getter and setter
 * 2. 类中必须要有一个公共的无参的构造器
 * 自动生成有参数构造器：右键 - generate - constructor
 * 自动生成无参数构造器: 右键 - generate - constructor - select None
 * 3. 没有其它方法
 *
 * 应用场景：
 * 实体类只负责数据存储，而对数据的处理交给其它类来完成，以实现数据和数据业务处理相分离
 */

public class Student {
    private String name;
    private double score;

    public Student() {
    }

    public Student(String name, double score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }
}
