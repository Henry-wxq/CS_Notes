package com.henryw.swing;

import javax.swing.*;
import java.awt.*;

public class Main2 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Hello Swing"); // 默认窗口不可见，快速设置窗口标题
        frame.setBounds(100, 100, 400, 300); // 设置窗口位置和大小, 单位: 像素, 2560 * 1600
        // frame.setLayout(null); // 设置为null，就可以自己设置组件位置

        // 多面板和分割面板
        // 多面板
        JTabbedPane tabbedPane = new JTabbedPane(); // 把组件装进去，可以装多个
        tabbedPane.setBounds(0, 0, 400, 300);
        tabbedPane.addTab("Tab 1", new JButton("Button 1"));
        tabbedPane.addTab("Tab 2", new JColorChooser());
        tabbedPane.addTab("Tab 4", new JFileChooser());
        tabbedPane.addTab("Tab 4", new JPanel(){{setBackground(Color.ORANGE);}});

        // 分割面板
        JSplitPane splitPane = new JSplitPane(); // 分割面板
        splitPane.setOrientation(JSplitPane.VERTICAL_SPLIT); // 设置分割方向
        splitPane.setLeftComponent(new JButton("Left")); // 设置左边组件
        splitPane.setRightComponent(new JButton("Right")); // 设置右边组件
        tabbedPane.addTab("Tab 3", splitPane); // 把分割面板添加到选项卡面板中

        frame.add(tabbedPane);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 关闭窗口，退出程序
        frame.setVisible(true);
    }
}
