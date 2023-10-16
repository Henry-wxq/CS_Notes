package com.henryw.interfacedemo1;

public interface A {
    // 成员变量(默认为常量，需要赋值),前面可以不加public static final
    String SCHOOL_NAME = "UOT";

    // 成员方法(默认为抽象方法，不能写方法体)，前面可以不加public abstract
    void test();
}

