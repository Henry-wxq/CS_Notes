package com.henryw.swing;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Main3 {
    public static void main(String[] args) {
        // 创建窗口对象
        JFrame frame = new JFrame(); // 默认窗口不可见

        // 设置窗口属性
        frame.setSize(400, 300); // 设置窗口大小, 单位: 像素, 2560 * 1600
        frame.setAlwaysOnTop(true); // 窗口总在最前面


        frame.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE); // 关闭窗口，退出程序

        // 自己处理关闭
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                // 弹一个对话框，确认关闭
                JOptionPane.showConfirmDialog(frame, "Are you sure?", "Confirm", JOptionPane.YES_NO_OPTION);
            }
        });


        frame.setVisible(true); // 默认窗口在屏幕左上角(0, 0)位置
    }
}
