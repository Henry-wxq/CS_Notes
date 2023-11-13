package com.henryw.mathdemo1;

/**
 * Math: 代表数学，是一个工具类，里面提供的都是对数据进行操作的一些静态方法
 *
 * 常用方法
 * 1. 获取参数绝对值： int abs(int a); double abs(double a)
 * 2. 向上取整： double ceil(double a)
 * 3. 向下取整： double floor(double a)
 * 4. 四舍五入： int round(float a)
 * 5. 获取两个int值中较大值： int max(int a, int b)
 * 6. 返回a的b次幂的值： double pow(double a, double b)
 * 7. 返回值为double的随机值，范围[0.0, 1.0)： double random()
 */

public class Test {
    public static void main(String[] args) {
        // 1. abs(int a); abs(double a)
        System.out.println(Math.abs(-12)); // 12
        System.out.println(Math.abs(123)); // 123
        System.out.println(Math.abs(-3.1)); // 3.1

        // 2. ceil(double a)
        System.out.println(Math.ceil(4.00001)); // 5.0
        System.out.println(Math.ceil(4.0)); // 4.0

        // 3. floor(double a)
        System.out.println(Math.floor(4.999)); // 4.0
        System.out.println(Math.floor(5.0)); // 5.0

        // 4. int round(float a)
        System.out.println(Math.round(4.4)); // 4 注意，返回值为int
        System.out.println(Math.round(4.5)); // 5

        // 5. max(int a, int b)
        System.out.println(Math.max(10, 200)); // 200
        System.out.println(Math.min(10, 200)); // 10

        // 6. pow(double a, double b)
        System.out.println(Math.pow(2, 3)); // 8.0

        // 7. random()
        System.out.println(Math.random());

    }
}
