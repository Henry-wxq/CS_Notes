package com.henryw.abstractdemo2;

public abstract class Animal {
    private String name;

    public abstract void cry(); // 有抽象方法的类就是抽象类

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
