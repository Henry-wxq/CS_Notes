package com.henryw.stringbuilderdemo4;

// 需求：设计一个方法，用于返回任意整形数组的内容，要求返回的数组内容格式如: [11, 22, 33]

public class Test4 {
    public static void main(String[] args) {
        System.out.println(getArrayData(new int[]{11, 22, 33}));
    }

    public static String getArrayData(int[] arr){
        // 1. 判断arr是否为null
        if (arr == null) {
            return null;
        }

        // 2. arr数组对象存在。arr = [11, 22, 33]
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < arr.length; i++) {
            if (i == arr.length - 1){
                sb.append(arr[i]);
            } else {
                sb.append(arr[i]).append(", ");
            }
        }
        sb.append("]");

        return sb.toString();
    }
}
