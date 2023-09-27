package com.henryw.branch;

/**
 * switch分支通过比较值来决定执行哪条分支
 * 执行流程：
 * 1. 先执行表达式的值，再拿着这个值去与case后的值进行匹配
 * 2. 与哪个case后的值匹配为true就执行哪个case块的代码，遇到break就跳出switch分支
 * 3. 如果全部case后的值与之相匹配都是false，则执行default块的代码
 *
 * 应用场景：
 * 1. 当条件是一个一个值比较的时候，switch分支更合适：格式良好，性能较好
 * 2. 当条件是区间的时候，应该用if分支
 */

public class SwitchDemo2 {
    public static void main(String[] args) {
        // 每天做不一样的事情
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
                break;
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
    }
}
