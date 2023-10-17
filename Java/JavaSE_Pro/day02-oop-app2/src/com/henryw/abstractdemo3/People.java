package com.henryw.abstractdemo3;

/**
 * 设计模板方法设计模式
 * 1. 定义一个模板方法出来
 */

public abstract class People {
    public final void write(){
        System.out.println("\t\t\t\t\t 《我的爸爸》");
        System.out.println("第一段");
        // 模板方法斌不清楚正文部分到底应该怎么写，但是它知道子类肯定要写
        System.out.println(writeMain());
        System.out.println("结尾部分");
    }

    public abstract String writeMain();
}
