package com.henryw.abstractdemo2;

public class Cat extends Animal{

    @Override
    public void cry() {
        System.out.println(getName() + "喵喵喵的叫");
    }
}
