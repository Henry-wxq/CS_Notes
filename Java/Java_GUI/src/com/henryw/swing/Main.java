package com.henryw.swing;

/**
 * Swing: Java GUI, 基于AWT
 */

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // 创建窗口对象
        JFrame frame = new JFrame("Hello Swing"); // 默认窗口不可见，快速设置窗口标题

        // 设置窗口大小, 单位: 像素, 2560 * 1600
        frame.setSize(400, 300);

        // 设置窗口layout, 默认是BorderLayout
        frame.setLayout(null); // 设置为null，就可以自己设置组件位置

        // 设置默认关闭操作, 不用写监听器了
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 关闭窗口，退出程序
        // frame.setDefaultCloseOperation(WindowConstants.HideOnClose); // 并不关闭，只是隐藏
        // frame.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE); // 什么都不做
        // frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE); // 释放窗口占用的资源，但不会关闭程序

        // 按钮
        JButton button = new JButton("Click me");
        button.setBounds(0, 0, 280, 30); // 设置按钮位置和大小,在窗口原点标题栏下方，而不是直接在窗口左上角，不会被标题栏挡住了

        // 按钮增加监听器
        button.addActionListener(e -> {
            System.out.println("Button clicked");
        });

        // 设置菜单栏
        JMenuBar bar = new JMenuBar();
        JMenu menu = new JMenu("File");
        JMenuItem item = new JMenuItem("Open");

        // 添加菜单项监听器
        item.addActionListener(e -> {
            System.out.println("Open selected");
        });
        menu.add(item);

        menu.add(new JMenuItem("File"));
        menu.add(new JMenuItem("Edit"));
        bar.add(menu);
        frame.setJMenuBar(bar);

        // Swing新增组件
        // 进度条

        // 开关按钮

        // 颜色选择器
//        JComponent colorChooser = new JColorChooser();
//        colorChooser.setBounds(0, 30, 280, 30);
//        frame.add(colorChooser);

        // 文件选择器
//        JFileChooser fileChooser = new JFileChooser();
//        fileChooser.setBounds(30, 30, 280, 30);
//        frame.add(fileChooser);

        // 工具提示
        button.setToolTipText("Click me and see what happens");

        // 添加按钮到窗口
        frame.add(button); // 添加按钮到窗口，有默认UI，可以换

        // 展示窗口
        frame.setVisible(true); // 默认窗口在屏幕左上角(0, 0)位置
    }
}
