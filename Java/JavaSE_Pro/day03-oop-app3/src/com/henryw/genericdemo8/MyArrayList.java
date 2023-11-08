package com.henryw.genericdemo8;

// 泛型类
public class MyArrayList<E> {
    // ArrayList怎么保存数据？
    // 其实声明了一个Object类型的数组
    private Object[] arr = new Object[10]; // 超过了再说
    private int size; // 记录当前位置

    public boolean add(E e){ // e为形参
        arr[size++] = e;
        return true;
    }

    public E get(int index){
        return (E) arr[index];
    }
}
