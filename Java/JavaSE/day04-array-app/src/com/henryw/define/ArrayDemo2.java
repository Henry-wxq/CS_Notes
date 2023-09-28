package com.henryw.define;

/**
 * 数组的访问
 * 数组名字[索引]
 */

public class ArrayDemo2 {
    public static void main(String[] args) {
        int[] arr = {12, 24, 36};
                    //0  1   2

        // 1. 访问数组的全部数据
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);

        // 2. 修改数组中的数据
        arr[0] = 66;
        arr[2] = 100;
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);

        // 3. 访问数组的元素个数：数组名.length
        System.out.println(arr.length);

        // 4. 获取数组的最大索引: 长度减一，前提是数组中存在至少一个元素
        System.out.println(arr.length - 1);
    }
}
