package com.henryw.innerclassdemo4;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * 匿名内部类再开发中的真实使用场景
 * 通过GUI介绍
 */

public class Test {
    public static void main(String[] args) {
        // GUI编程：桌面编程
        // 1. 创建窗口
        JFrame win = new JFrame("登录界面");
        JPanel panel = new JPanel();
        win.add(panel);

        JButton btn = new JButton("登录");
        win.add(btn);

        // 给按钮绑定单击事件监听器，需要一个监听器对象
        // 使用匿名内部类，当调用别人的API时刚好是个接口对象，需要用的时候才要用
//        btn.addActionListener(new ActionListener() {
//            @Override
//            public void actionPerformed(ActionEvent e) {
//                JOptionPane.showMessageDialog(win, "登陆一下");
//            }
//        });
        // 核心目的是简化代码，后续匿名内部类就可以简化成一行，用lamada表达式
        btn.addActionListener(e -> JOptionPane.showMessageDialog(win, "登陆一下"));


        win.setSize(400, 400);
        win.setLocationRelativeTo(null);
        win.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        win.setVisible(true);
    }
}
