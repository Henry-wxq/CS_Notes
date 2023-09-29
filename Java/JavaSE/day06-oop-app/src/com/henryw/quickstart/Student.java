package com.henryw.quickstart;

/**
 * 面向对象编程：先创建一个类结构，开发一个个对象，把数据交给对象，再调用对象的方法来完成对数据的处理
 * class也就是类，也成为对象的设计图(或者对象的模板)
 * 这里相当于是一张空的学生表
 * Test.java中相当于是给两个学生表中添上了数据
 *
 * 注意事项：
 * 1. 类名建议使用英文单词，首字母大写，满足驼峰属性，且要具有意义，如，Car，Student
 * 2. 类中定义的变量也成为成员变量，类中定义的方法也成为成员方法
 * 3. 成员变量本身存在默认值，不要赋初始值，因为没有意义
 * 4. 一个代码文件中，可以写多个class类，但是只能用一个public修饰，且public修饰的类名必须成为代码的文件名
 * 5. 对象与对象之间的数据不会相互影响，但是多个变量指向的同一个对象时就会相互影响了
 * 6. 如果某个对象没有一个变量引用它，则该对象无法被操作，该对象会成为所谓的垃圾对象，比如先创建一个对象，但赋值成null，栈内存中的变量存
 * 储的对象地址就会变成null，堆内存中的对象就没有变量指向，就成为了垃圾对象
 */

public class Student {
    // 打印学生总成绩，平均成绩
    // 先定义变量
    String name; // 姓名
    double chinese; // 语文成绩
    double math; // 数学成绩

    // 然后定义方法
    public void printTotalScore() {
        System.out.println(name + "的总成绩是: " + (chinese + math));
    }

    public void printAverageScore() {
        System.out.println(name + "的平均成绩是: " + (chinese + math) / 2);
    }
}
