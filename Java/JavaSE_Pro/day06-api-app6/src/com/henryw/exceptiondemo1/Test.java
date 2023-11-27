package com.henryw.exceptiondemo1;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * 异常：异常就是代表程序出现的问题
 *                            Java.lang.Throwable(祖宗)
 *                            /                     \
 *                         Error                 Exception
 *                                              /          \
 *                                 RuntimeException      其它异常
 * Error: 代表的系统级别的错误(属于严重问题)也就是说系统一旦出现问题，sun公司会把这些问题封装成Error对象给出来，说白了，Error是给sun公
 * 司自己用的，不是给我们程序员用的
 * Exception: 异常，代表的是程序可能出现的问题，所以通常会用Exception以及它的子类来封装程序出现的问题
 * - 运行时异常：RuntimeException及其子类，编译阶段不会出现错误提醒，运行时出现的异常(如数组索引越界异常)
 * - 编译时异常: 编译阶段就会出现错误提醒的(如：日期解析异常)
 *
 * 处理异常
 * 1. 抛出异常 (throws)：在方法上使用throws关键字，可以将方法内部出现的异常抛出去给调用者处理
 * 方法 throws 异常1， 异常2， 异常3 ... {
 *     // ...
 * }
 * 2. 捕获异常 (try...catch)：直接捕获程序出现的异常
 * try {
 *     // 监视可能出现异常的代码
 * }catch(异常类型1 变量){
 *     // 处理异常
 * }catch(异常类型2 变量){
 *     // 处理异常
 * }
 *
 */

public class Test {
    public static void main(String[] args) throws ParseException{
//      SimpleDateFormat sdf = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
//      Date d = sdf.parse("2028-11-11 10:24");
//      // 想要不报错，有两种方法
//      // 1. 先检查代码有没有问题，没问题的话选中这一块儿代码，按住ctrl + alt + t，选择try/catch
        // 2. 在方法的位置后面写上throws ParseException，或者alt + enter快速写出
        // - 相当于让main方法去找最上层程序，i.e. JVM虚拟机，异常就会抛给JVM虚拟机处理，所以JVM会在内部用try/catch抓住然后打印异常信息
//      System.out.println(d);

//      try {
//          SimpleDateFormat sdf = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
//          Date d = sdf.parse("2028-11-11 10:24");
//          System.out.println(d);
//      } catch (ParseException e) {
//          throw new RuntimeException(e);
//      }

        SimpleDateFormat sdf = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
        Date d = sdf.parse("2028-11-11 10:24");
        System.out.println(d);
    }
}
