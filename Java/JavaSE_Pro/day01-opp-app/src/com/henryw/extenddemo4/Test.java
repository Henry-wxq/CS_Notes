package com.henryw.extenddemo4;

/**
 * 方法重写：当子类觉得父类中的某个方法不好用，或者无法满足自己的需求时，子类可以重写一个方法名称，参数列表一样的方法，
 * 去覆盖父类的这个方法，这就是重写
 * 注意：重写后，方法的访问，Java会遵循就近原则
 *
 * 注意事项：
 * 1. 重写小技巧，使用Override注解，可以指定Java编译器，检查我们方法重写的格式是否正确，代码可读性也会更好
 * 2. 子类重写父类的方法时，访问权限必须大于或等于父类该方法的权限(public > protected > 缺省)，即若父类是protected，那子类重写只能用
 * public或者protected，一样最好
 * 3. 重写方法返回值类型看，必须与被重写方法的返回值一样，或者范围更小
 * 4，私有方法，静态方法不能被重写，如果重写会报错的
 */

public class Test {
    public static void main(String[] args) {
        B b = new B();
        b.print1();
        b.print2(2, 3);
    }
}
