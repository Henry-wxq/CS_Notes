package com.henryw.abstractdemo2;

public class Dog extends Animal{

    @Override
    public void cry() {
        System.out.println(getName() + "汪汪汪的叫");
    }
}
