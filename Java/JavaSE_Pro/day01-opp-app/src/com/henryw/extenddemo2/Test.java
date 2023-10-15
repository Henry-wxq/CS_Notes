package com.henryw.extenddemo2;

/**
 * 权限修饰符：
 * 1. private: 在本类中
 * 2. 缺省：在本类中，同一个包下的其它类中
 * 3. protected：在本类中；同一个包下的其它类中；任意包下的子类里
 * 4. public：在本类中；同一个包下的其他类中；任意包下的子类里；任意包下的任意类中
 */

public class Test {
    public static void main(String[] args) {
        Modifier m1 = new Modifier();
        // m1.privateMethod();
        m1.method();
        m1.protectedMathod();
        m1.publicMethod();
    }
}
