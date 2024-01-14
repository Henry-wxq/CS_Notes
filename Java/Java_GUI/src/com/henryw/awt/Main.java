package com.henryw.awt;

import java.awt.*;
import java.awt.event.*;

/**
 * AWT: Abstract Window Toolkit
 * 基本框架
 *
 */

public class Main {
    public static void main(String[] args) {
        // 创建窗口对象
        Frame frame = new Frame("Hello AWT"); // 默认窗口不可见, 传入窗口标题

        // 设置窗口属性
        frame.setSize(400, 300); // 设置窗口大小, 单位: 像素, 2560 * 1600
        // frame.setLocation(200, 200); // 设置窗口位置, 原点是屏幕左上角，y轴正方向是反着的，单位: 像素

        // 设置窗口位置在屏幕中间
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize(); // 获取屏幕大小
        int x = (int) screenSize.getWidth() / 2 - frame.getWidth() / 2; // 计算x轴位置
        int y = (int) screenSize.getHeight() / 2 - frame.getHeight() / 2; // 计算y轴位置
        frame.setLocation(x, y); // 设置窗口位置在屏幕中间

        // frame.setBounds(x, y, 400, 300); // 设置窗口位置和大小, 一次性完成

        frame.setBackground(Color.BLACK); // 设置背景颜色
        frame.setAlwaysOnTop(true); // 设置窗口置顶，永远展示在前面
        frame.setResizable(false); // 设置窗口大小不可变
        frame.setCursor(new Cursor(Cursor.CROSSHAIR_CURSOR)); // 设置鼠标样式

        // 监听器, 监听窗口关闭事件
        frame.addWindowListener(new WindowAdapter() {
            // 可以重写很多方法，这里只重写了一个
            @Override
            public void windowClosing(WindowEvent e) {
                System.out.println("Closed");
                frame.dispose(); // 释放窗口资源
                // frame.setVisible(false); // 隐藏界面
                // System.exit(0); // 退出程序
            }
        });

        // 监听器, 监听键盘事件
        frame.addKeyListener(new KeyAdapter() {
            // 可以重写很多方法，这里只重写了一个
            @Override
            public void keyPressed(KeyEvent e) {
                System.out.println("Pressed");
                System.out.println(e.getKeyChar()); // 获取按下的键
                System.out.println(e.getKeyCode()); // 获取按下的键的ASCII码
                System.out.println(e.getKeyLocation()); // 获取按下的键的位置
            }
        });

        // 监听器, 监听鼠标事件
        frame.addMouseListener(new MouseAdapter() {
            // 可以重写很多方法，这里只重写了一个
            @Override
            public void mouseClicked(MouseEvent e) {
                System.out.println("Clicked");
                System.out.println(e.getX()); // 获取鼠标点击的x轴坐标
                System.out.println(e.getY()); // 获取鼠标点击的y轴坐标
                System.out.println(e.getButton()); // 获取鼠标点击的按钮
                System.out.println(e.getClickCount()); // 获取鼠标点击的次数
            }
        });

        // 组件
        // 标签组件：就是一个string
        Label label = new Label("Hello World");


        // 滚动面板，也是一个容器，但是只能放一个组件，可以和Panel配合使用
        ScrollPane scrollPane = new ScrollPane();
        frame.add(scrollPane); // 把滚动面板添加到窗口中, 默认是一个白板因为没有添加组件

        // 展示窗口
        frame.setVisible(true); // 默认窗口在屏幕左上角(0, 0)位置
    }
}
