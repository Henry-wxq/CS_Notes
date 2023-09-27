package com.henryw.branch;

/**
 * switch使用时的注意事项
 */

public class SwitchDemo3 {
    public static void main(String[] args) {
        // 1. 表达式的类型只能是byte, short, int, char, JDK7开始支持String, 不支持double, float, long.
        // long: 范围太大
        // double: 运算不精确
        double b1 = 0.1;
        double b2 = 0.2;
        double c = b1 + b2;
        System.out.println(c);

        // 2. case给出的值不允许重复，且只能是字面量，不能是变量.
        int i = 20;
        int d = 10;  // 因为变量的值可能会发生改变
        switch (i) {
            case 10:
                break;
            case 20:
                break;
        }

        // 3. 正常使用switch时，不要忘了写break，不然会出现穿透现象
        // 会同时打出龙虾烧烤和今晚吃鸡
        String week = "周三";
        switch (week) {
            case "周一":
                System.out.println("埋头苦干，解决bug");
                break;
            case "周二":
                System.out.println("请教他人");
                break;
            case "周三":
                System.out.println("龙虾烧烤");
//                break;
            case "周四":
                System.out.println("今晚吃鸡");
                break;
            case "周五":
                System.out.println("帮助女程序员解决问题");
                break;
            case "周六":
                System.out.println("酒吧嗨皮");
                break;
            case "周日":
                System.out.println("郁郁寡欢，准备上班");
                break;
            default:
                System.out.println("星期不存在");
        }

        System.out.println("----------------------------------------------------------");

        // 4. 利用switch穿透性在情况下可以简化代码
        // 当存在多个case分支的代码相同时，可以把相同的代码放到一个case块中，只写一遍，其它的穿透到该case块执行代码即可
        // 周二周三周四都是请教他人，周六周日都是酒吧嗨皮
        String weekday = "周三";
        switch (weekday) {
            case "周一":
                System.out.println("埋头苦干，解决bug");
                break;
            case "周二":
            case "周三": // 当匹配到周三的时候，因为没有break存在，所以自动穿透执行周四的请教他人，简化代码
            case "周四":
                System.out.println("请教他人");
                break;
            case "周五":
                System.out.println("帮助女程序员解决问题");
                break;
            case "周六":
            case "周日":
                System.out.println("酒吧嗨皮");
                break;
            default:
                System.out.println("星期不存在");
        }
    }
}
