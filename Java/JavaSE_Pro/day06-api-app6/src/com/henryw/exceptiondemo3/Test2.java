package com.henryw.exceptiondemo3;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * 优化：不用抛具体的异常，直接抛exception
 */

public class Test2 {
    public static void main(String[] args) {
        try {
            test_1(); // 有异常，在最外层捕获异常，ctrl + alt + t
        } catch (Exception e) {
            System.out.println("您当前操作有问题"); // 相应一个友好的信息给用户
            e.printStackTrace(); // 打印出这个异常对象的信息，记录下来
        }
    }

    public static void test_1() throws Exception {
        SimpleDateFormat sdf = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
        Date d = sdf.parse("2028-11-11 10:24"); // 有异常，应该层层往外抛， alt + enter
        System.out.println(d);

        test_2(); // 抛上来，需要处理，继续alt + enter
    }

    public static void test_2() throws Exception { // 直接抛Exception
        // 读取文件的
        InputStream is = new FileInputStream("D:/meinv.png"); // 有异常，应该层层往外抛，alt + enter
    }

}
