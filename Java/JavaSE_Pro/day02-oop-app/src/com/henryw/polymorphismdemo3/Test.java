package com.henryw.polymorphismdemo3;

/**
 * 类型转换
 * 1. 自动类型转换：父类 变量名 = new 子类() e.g. People p = new Teacher();
 * 2. 强制类型转换：子类 变量名 = (子类) 父类变量 e.g Teacher t = (Teacher) p
 *
 * 强制类型转换的注意事项
 * 1. 存在继承/实现关系就可以在编译阶段进行强制类型转换，编译阶段不会报错
 * 2. 运行是，如果发现对象的真是类型与强转后的类型不同，就会报类型转换异常(ClassCastException)的错误出来
 *
 * 强转前，Java建议
 * 使用instanceof关键字，判断当前对象的真实类型，在进行强转
 */

public class Test {
    public static void main(String[] args) {
        People p1 = new Student();
        p1.run();

        // 强制类型转换
        Student s1 = (Student) p1;
        s1.exam();

        System.out.println("-------------------------------------------");

        // 编译阶段有继承或者实现关系就可以强制转换，但是运行时，可能出现类型转换异常
        // 因为在编译的时候，p1是People，看不到p1右边是Student，跑的时候才看到，就会有一场
        // Teacher t1 = (Teacher) p1; // 运行时出现了：ClassCastException

        // 用instanceof判断，再进行转换
        if (p1 instanceof Student) {
            Student s2 = (Student) p1;
            s2.exam();
        } else {
            Teacher t2 = (Teacher) p1;
            t2.teach();
        }

        System.out.println("-------------------------------------------");

        Student s = new Student();
        go(s);

        Teacher t= new Teacher();
        go(t);
    }

    public static void go(People p){
        p.run();
        if (p instanceof Student) {
            Student s = (Student) p;
            s.exam();
        } else if (p instanceof Teacher){
            Teacher t = (Teacher) p;
            t.teach();
        }
    }

}

