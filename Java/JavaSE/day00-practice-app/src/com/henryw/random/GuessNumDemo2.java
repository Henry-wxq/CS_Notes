package com.henryw.random;

import java.util.Random;
import java.util.Scanner;

/**
 * 需求：随即生成一个1~100的数据，提示用户猜测，猜大提示过大，猜小提示过小
 */

public class GuessNumDemo2 {
    public static void main(String[] args) {
        
        Random r = new Random();
        int num_guess = r.nextInt(100) + 1;

        Scanner sc = new Scanner(System.in);
        
        while (true) {
            System.out.println("请输入您猜测的数字：");
            int temp_guess = sc.nextInt();
            
            if (temp_guess < num_guess) {
                System.out.println("猜测的数字小了！");
            } else if (temp_guess > num_guess) {
                System.out.println("猜测的数字大了！");
            } else {
                System.out.println("买单的就是你！");
                break;
            }
        }
    }
   
    
    
}
