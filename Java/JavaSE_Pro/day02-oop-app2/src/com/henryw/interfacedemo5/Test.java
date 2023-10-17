package com.henryw.interfacedemo5;

/**
 * 接口的多继承
 *
 * 便于实现类去实现
 *
 * 注意事项
 * 1. 一个接口继承多个接口，如果接口中存在方法签名冲突，则此时不支持多继承
 * 2. 一个类实现多个接口，如果接口中存在方法签名冲突，则此时不支持多实现
 * 3. 一个类继承了父类，有同时实现了接口，父类和接口中有永明的默认方法，实现类会优先用父类的
 * 4. 一个类实现了多个接口，多个接口中存在同名的默认方法，可以不冲突，这个类重写该方法即可
 */

public class Test {
    public static void main(String[] args) {

    }
}

interface A{}
interface B{}
interface C{}
interface D extends A, B, C{}

//class E implements A, B, C{}
class E implements D{}