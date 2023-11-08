package com.henryw.genericdemo9;

import java.util.ArrayList;

// 泛型接口
// 既可能保存学生对象，又可能保存老师对象，所以考虑使用泛型
public interface Data<E> {
    void add(E e);

    ArrayList<E> getByName(String name);
}
