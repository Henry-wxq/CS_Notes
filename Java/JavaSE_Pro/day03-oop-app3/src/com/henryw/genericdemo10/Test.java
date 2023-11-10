package com.henryw.genericdemo10;

import java.lang.reflect.Array;
import java.util.ArrayList;

/**
 * 泛型方法
 * 修饰符 <类型变量, 类型变量, ...> 返回值类型 方法名(形参列表) {
 *
 * }
 *
 * e.g. 是泛型方法
 * public static <T> void test(T t){
 * }
 *
 * e.g. 不是泛型方法，因为没有自己定义泛型变量
 * public E get(int index){
 *      return (E) arr[index];
 * }
 *
 * 通配符：？
 * 可以在"使用泛型"的时候代表一切类型；ETKV实在定义泛型的时候使用
 *
 * 泛型的上下限
 * 上限：? extends Car (? 能接收的必须是Car或者其子类)
 * 下限：? super Car (? 能接收的必须是Car或者其父类)
 */

public class Test {
    public static void main(String[] args) {
        String rs = test("Java");
        System.out.println(rs);

        Dog d = test(new Dog());
        System.out.println(d);

        // 需求：所有的汽车可以一起参加比赛
        ArrayList<Car> cars = new ArrayList<>();
        cars.add(new BMW());
        cars.add(new Benz());
        go(cars);

        ArrayList<BMW> bmws = new ArrayList<>();
        bmws.add(new BMW());
        bmws.add(new BMW());
        // go(bmws); // 报错，因为ArrayList没有关系
        // go2(bmws); // 可以送进来，但是没有限制送进来的类型
        go3(bmws);

        ArrayList<Benz> benz = new ArrayList<>();
        benz.add(new Benz());
        benz.add(new Benz());
        // go(benz); // 报错，因为ArrayList没有关系
        // go2(bmws); // 可以送进来，但是没有限制送进来的类型
        go3(benz);

        ArrayList<Dog> dogs = new ArrayList<>();
        dogs.add(new Dog());
        dogs.add(new Dog());
        go2(dogs); // 可以送进来，但是没有限制送进来的类型
        // go3(dogs) // 报错
    }

    // 泛型方法
    public static <T> T test(T t){
        return t;
    }

    // j
    public static void go(ArrayList<Car> cars){

    }

    public static <T> void go2(ArrayList<T> cars){

    }


    public static <T extends Car> void go3(ArrayList<T> cars) { // 限制只能接收extends类型的

    }

    // 与go3作用相同
    public static void go4(ArrayList<? extends Car> cars) { // 不自己定义泛型，用问号代替一切泛型

    }
}
