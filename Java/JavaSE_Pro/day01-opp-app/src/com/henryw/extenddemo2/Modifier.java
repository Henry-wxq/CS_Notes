package com.henryw.extenddemo2;

public class Modifier {
    // 1. private: 在本类中
    private void privateMethod(){
        System.out.println("--private--");
    }

    // 2. 缺省：在本类中，同一个包下的其它类中
    void method(){
        System.out.println("--缺省--");
    }

    // 3. protected：在本类中；同一个包下的其它类中；任意包下的子类里
    protected void protectedMathod(){
        System.out.println("--protected");
    }

    // 4. public：在本类中；同一个包下的其他类中；任意包下的子类里；任意包下的任意类中
    public void publicMethod(){
        System.out.println("--public--");
    }

    // 本类中访问
    public void test() {
        privateMethod();
        method();
        protectedMathod();
        publicMethod();
    }
}
