package com.henryw.loop;

public class NestedLoopDemo7 {
    public static void main(String[] args) {
        // 三天，每天说五句我爱你
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 5; j++) {
                System.out.println("我爱你");
            }
            System.out.println("-----------------------------------------------");
        }

        // 每行打印4个*，打印3行
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 4; j++) {
                System.out.print("*"); // 去掉ln以后就不会换行了
            }
            System.out.println();
        }
    }
}
