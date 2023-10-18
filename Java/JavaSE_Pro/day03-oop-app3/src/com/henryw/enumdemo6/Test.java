package com.henryw.enumdemo6;

/**
 * 枚举的应用场景
 * 做信息标志和分类
 * 选择枚举表示一组信息，并作为参数传输
 */

public class Test {
    public static void main(String[] args) {
//        check(1);
//        check(Constant.BOY); // 防止乱放数据

        check(Constant2.BOY); // 不能乱填，因为是枚举
    }

//    public static void check(int sex){
//        switch (sex) {
//            case Constant.BOY:
//                System.out.println("展示一些游戏图片");
//                break;
//            case Constant.GIRL:
//                System.out.println("展示一些帅哥图");
//                break;
//        }
//    }

    public static void check(Constant2 sex){
        switch (sex) {
            case BOY: // 不用带前缀
                System.out.println("展示一些游戏图片");
                break;
            case Girl:
                System.out.println("展示一些帅哥图");
                break;
        }
    }
}
