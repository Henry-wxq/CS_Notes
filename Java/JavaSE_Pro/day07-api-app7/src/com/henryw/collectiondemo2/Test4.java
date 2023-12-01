package com.henryw.collectiondemo2;

import java.util.ArrayList;
import java.util.Collection;

/**
 * 遍历集合中的自定义对象
 *
 * 需求
 * 展示多部电影信息
 *
 * 分析
 * 每部电影都是一个对象，多部电影要使用集合转起来
 * 遍历集合中的三个电影对象，输出每部电影的详细信息
 */

public class Test4 {
    public static void main(String[] args) {
        // 创建集合对象
        Collection<Movie> c = new ArrayList<>();

        // 创建电影对象
        Movie m1 = new Movie("The Shawshank Redemption", 9.6, "Frank Darabont");
        Movie m2 = new Movie("The Godfather", 9.2, "Francis Ford Coppola");
        Movie m3 = new Movie("The Dark Knight", 9.0, "Christopher Nolan");

        // 将电影对象添加到集合中
        c.add(m1);
        c.add(m2);
        c.add(m3);
        System.out.println(c); // 输出的是集合中的对象的地址，如果需要输出详细内容，需要重写toString方法

        // 遍历集合
        for (Movie movie : c) {
            System.out.println("电影名: " + movie.getName());
            System.out.println("评分: " + movie.getScore());
            System.out.println("导演: " + movie.getDirector());
        }

        c.forEach(System.out::println);
    }
}
