package com.henryw.exceptiondemo2;

/**
 * 必须让这个类继承自RuntimeException
 */

// 自定义运行时异常
public class AgeIllegalException extends Exception{
    // 先选前两个构造器
    public AgeIllegalException() {
    }

    // message封装报错原因
    public AgeIllegalException(String message) {
        super(message);
    }
}
