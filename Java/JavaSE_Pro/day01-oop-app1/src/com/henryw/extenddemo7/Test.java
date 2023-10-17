package com.henryw.extenddemo7;

/**
 * 子类构造器的特点：子类的全部构造器，都会先调用父类的构造器，再执行自己
 * 子类构造器，默认存在super(); 默认调用父类的无参构造器
 *
 * 若手写父类有参构造器，干掉父类无参构造器，子类构造器会报错，需要再子类构造器中第一行手写调用父类的有参构造器
 * e.g. super("Henry", 20);
 */

class F{
    public F(){
        System.out.println("--父类的无参构造器 执行了--");
    }
}

class Z extends F{
    public Z(){
        // 默认存在super(); 默认调用父类的无参构造器
        System.out.println("--子类的无参构造器 执行了--");
    }

    public Z(String name){
        // 默认存在super(); 默认调用父类的无参构造器
        System.out.println("--子类的有参构造器 执行了--");
    }
}

public class Test {
    public static void main(String[] args) {
        Z z1= new Z();
        Z z2 = new Z("Henry");
    }
}
