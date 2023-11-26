package com.henryw.runtimedemo3;

import java.io.IOException;

/**
 * Runtime代表程序所在的运行环境，是一个单例类，对外只有一个对象，应用程序无法创建自己的对象
 *
 *
 */

public class Test {
    public static void main(String[] args) throws IOException, InterruptedException {
        // 1. 返回与当前Java应用程序关联的运行时对象
        Runtime r = Runtime.getRuntime(); // 单例类

        // 2. 终止当前运行的虚拟机，该参数用作状态代码，按照惯例，非零状态代码表示异常终止
        // public void exit(int status)
        // r.exit(0);

        // 3. 获取虚拟机能够使用的处理器数量
        // public int availableProcessors()
        System.out.println(r.availableProcessors());

        // 4. 返回Java虚拟机中的内存总量，单位是字节，1024 = 1kb 1024 * 1024 = 1M
        // public long totalMemory()
        System.out.println(r.totalMemory() / 1024.0 / 1024.0 + "MB");

        // 5. 返回Java虚拟机中的可用内存量
        // public long freeMemory()
        System.out.println(r.freeMemory() / 1024.0 / 1024.0 + "MB");

        // 6. 启动某个程序，并返回代表该程序的对象
        // public Process exec(String command)
        // 如果程序名称已经配置到了系统环境变量中，那么可以直接填写名字，不然需要填写绝对路径
        Process p = r.exec("C:\\Soft\\Utilities\\7-Zip");
        Thread.sleep(5000); // 让程序在这里暂停5s后继续往下走
        p.destroy(); // 关闭程序
    }
}
