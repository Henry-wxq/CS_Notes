package com.henryw.exceptiondemo2;

/**
 * 自定义异常
 * Java无法为这个世界上全部的问题都提供异常类来代表，如果企业自己的某种问题，想通过异常来表示，以便用异常来管理该问题，那就需要自己来定义异常了
 *
 * 自定义异常的种类
 * 1. 自定义运行时异常(RuntimeException)
 *  - 定义一个异常类继承RuntimeException
 *  - 重写构造器
 *  - 通过throw new 异常类(xxx) 来创建异常对象并抛出
 *
 * 2. 自定义编译时异常
 *  - 定义一个异常类继承Exception
 *  - 重写构造器
 *  - 通过throw new 异常类(xxx)来创建异常对象并抛出
 *
 *  很容易犯的错误，使用编译时异常
 *  不容易犯的错误，使用运行时异常
 */

public class Test {
    public static void main(String[] args) {
        // 需求：保存一个合法的年龄
        try {
            // 自定义运行时异常
            saveAge1(160); // ctrl + alt + t
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("底层出现了bug");
        }

        try {
            saveAge2(25); // 直接写会报错
        } catch (AgeIllegalException e) {
            e.printStackTrace();
            System.out.println("saveAge2底层有bug");
        }
    }

    public static void saveAge1(int age){
        if (age > 0 && age < 150) {
            System.out.println("Age saved Successfully: " + age);
        }else {
            // System.out.println("Unsuccessfully"); // 非常不专业
            // 用一个异常对象来封装这个问题
            // throw: 抛出去这个异常对象
            throw new AgeIllegalRuntimeException("/age is illegal, your age is " + age);
        }
    }

    public static void saveAge2(int age) throws AgeIllegalException {
        if (age > 0 && age < 150) {
            System.out.println("Age saved Successfully: " + age);
        }else {
            // System.out.println("Unsuccessfully"); // 非常不专业
            // 用一个异常对象来封装这个问题
            // 抛给上层调用者，即如果main中调用saveAge2，则会报错
            throw new AgeIllegalException("/age is illegal, your age is " + age); // 一些出来就会报错
        }
    }
}
