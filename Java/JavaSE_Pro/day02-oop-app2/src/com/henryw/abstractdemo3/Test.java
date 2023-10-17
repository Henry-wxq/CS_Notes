package com.henryw.abstractdemo3;

/**
 * 搞清楚抽象类的应用场景之一：经常用来设计模板方法模式
 * 1. 定义一个抽象类
 * 2. 里面定义两个方法
 *      1. 一个是模板方法，把相同的代码放里面去
 *      2. 一个是抽象方法，具体实现交给子类完成
 *
 * 建议使用final方法修饰模板方法，防止方法被子类重写
 */

public class Test {
    public static void main(String[] args) {
        // 场景：学生，老师都要写一篇作文：我的爸爸
        // 第一段是一样的；
        // 正文部分自由发挥(中间的代码不一样，但是高度重合)
        // 最后一段是一样的
        Teacher t = new Teacher();
        t.write(); // 写作文的方法并不是writeMain而是write
    }
}
