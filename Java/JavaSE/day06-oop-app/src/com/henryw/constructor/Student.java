package com.henryw.constructor;

/**
 * 构造器：名称与类名相同，前面只有public，没有返回值类型
 * 同样可以进行方法重构
 *
 * 构造器的特点：
 * 1. 创建对象时，对象会去调用构造器
 *
 * 构造器的运用场景：
 * 1. 创建对象时，同时可以完成对对象成员变量(属性)的初始化赋值，就可以省略s1.name; s1.score一个个的赋值
 *
 * 注意事项：
 * 1. 类在设计时，如果不写构造器，Java会为类自动生成一个无参构造器的
 * 2. 一旦定义了有参数构造器，Java就不会帮我们的类自动生成无参构造器了，此时就建议自己手写一个无参数构造器出来了，因为别人可能会需要使用
 */

public class Student {

    String name;
    double score;

    // 无参数构造器
    public Student() {
        System.out.println("无参数构造器被触发了");
    }

    // 有参数构造器
    public Student(String name, double score) {
        System.out.println("有参数构造器被触发了");
        this.name = name;
        this.score = score;
    }
}
