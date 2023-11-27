package com.henryw.exceptiondemo2;

/**
 * 必须让这个类继承自RuntimeException
 */

// 自定义运行时异常
public class AgeIllegalRuntimeException extends RuntimeException{
    // 先选前两个构造器
    public AgeIllegalRuntimeException() {
    }

    // message封装报错原因
    public AgeIllegalRuntimeException(String message) {
        super(message);
    }
}
