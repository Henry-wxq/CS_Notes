package com.henryw.branch;

/**
 * if, else if, else
 *
 * 若只有if，else，可以使用三元运算符，更加的专业
 */

public class IfDemo1 {
    public static void main(String[] args) {
        // 打分系统，D: [0, 60), C: [60, 70), B: [70, 80), A: [80, 90), S: [90, 100)
        double score = 85.5;

        if (score >= 0 && score < 60) {
            System.out.println('D');
        } else if (score >= 60 && score < 70) {
            System.out.println('C');
        } else if (score >= 70 && score < 80) {
            System.out.println('B');
        } else if (score >= 80 && score < 90) {
            System.out.println('A');
        } else if (score >= 90 && score < 100){
            System.out.println('S');
        } else {
            System.out.println("分数有毛病");
        }
    }
}
