package com.henryw.loop;

/**
 * 不知道要循环多少次的案例
 */

public class WhileDemo4 {
    public static void main(String[] args) {
        // 纸张折叠长珠穆朗玛峰需要多少次？
        double peakHeight = 8848860;
        double paperThickness = 0.1;

        int num = 0;
        while (paperThickness < peakHeight) {
            paperThickness *= 2;
            num++;
        }
        System.out.println("需要折叠" + num + "次");
        System.out.println("纸张最后" + paperThickness + "厚");
    }
}
