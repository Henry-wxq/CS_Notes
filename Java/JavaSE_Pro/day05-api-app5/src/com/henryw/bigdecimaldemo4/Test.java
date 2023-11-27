package com.henryw.bigdecimaldemo4;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * BigDecimal用于解决浮点型运算是，出现结果失真的问题
 *
 * 构造器
 * 1. public BigDecimal(double val) (不推荐，没区别，把double转换成BigDecimal)
 * 2. public BigDecimal(String val) (推荐使用，把String转成BigDecimal)：拆成一个数组，每一位进行计算
 *
 */

public class Test {
    public static void main(String[] args) {
        // 精度失真
        double a = 0.1;
        double b = 0.2;
        double c = a + b; // 0.30000000000000004
        System.out.println(c);
        System.out.println("-------------------------------------");

        // 使用构造器，编程字符串，封装成BigDecimal对象
//        BigDecimal a1 = new BigDecimal(Double.toString(a));
//        BigDecimal b1 = new BigDecimal(Double.toString(b));

        // 不使用构造器，直接使用方法把小数转换成字符串再得到BigDecimal对象来使用(推荐方式)
        BigDecimal a1 = BigDecimal.valueOf(a);
        BigDecimal b1 = BigDecimal.valueOf(b);

        // 方法: add, subtract, multiply, divide,
        BigDecimal c1 = a1.add(b1); // 0.3
        System.out.println(c1); // 没有输出地址，说明重写了toString方法
        BigDecimal c2 = a1.subtract(b1); // -0.1
        BigDecimal c3 = a1.multiply(b1); // 0.02
        BigDecimal c4 = a1.divide(b1); // 0.5

        // 当不能整除的时候
        BigDecimal i = BigDecimal.valueOf(0.1);
        BigDecimal j = BigDecimal.valueOf(0.3);
        BigDecimal k = i.divide(j, 2, RoundingMode.HALF_UP); // public BigDecimal divide (另一个BigDecimal对象，精确几位，舍入对象)

        // BigDecimal只是手段，double才是目的
        // public double doubleValue()
        double rs = k.doubleValue();
        System.out.println(rs);




    }
}
