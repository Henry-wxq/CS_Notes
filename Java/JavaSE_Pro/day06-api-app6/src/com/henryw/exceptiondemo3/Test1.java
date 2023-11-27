package com.henryw.exceptiondemo3;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * 开发中对于异常的常见处理方式 (从下向上)
 *      方法A ----------------> 1. A捕获异常，记录异常并相应合适的信息给用户
 *        |                    2. 捕获异常，尝试重新修复
 *      方法B 异常，抛给调用者
 *        |
 *      方法C 异常，抛给调用者
 */

public class Test1 {
    public static void main(String[] args) {
        try {
            test_1(); // 有异常，在最外层捕获异常，ctrl + alt + t
        } catch (FileNotFoundException e) {
            System.out.println("您要找的文件不存在"); // 相应一个友好的信息给用户
            e.printStackTrace(); // 打印出这个异常对象的信息，记录下来
        } catch (ParseException e) {
            System.out.println("您要解析的时间有问题了");
            e.printStackTrace();
        }
    }

    public static void test_1() throws FileNotFoundException, ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
        Date d = sdf.parse("2028-11-11 10:24"); // 有异常，应该层层往外抛， alt + enter
        System.out.println(d);

        test_2(); // 抛上来，需要处理，继续alt + enter
    }

    public static void test_2() throws FileNotFoundException {
        // 读取文件的
        InputStream is = new FileInputStream("D:/meinv.png"); // 有异常，应该层层往外抛，alt + enter
    }

}
