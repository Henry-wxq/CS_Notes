package com.henryw.enumdemo5;

/**
 * 抽象枚举：在枚举里面定义了一个抽象方法
 */

public enum B {
    // 因为枚举里面是抽象方法，不能直接创建对象
    X(){
        @Override
        public void go(){

        }
    },  Y("Henry"){
        @Override
        public void go(){
            System.out.println(getName() + "在学");
        }
    },  Z(){
        @Override
        public void go(){

        }
    };

    private String name;

    B(){}

    B(String name) {
        this.name = name;
    }

    public abstract void go();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
