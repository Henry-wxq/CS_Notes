package com.henryw.string;

/**
 * String常用方法
 */

public class StringDemo2 {
    public static void main(String[] args) {
        String s = "Henryw";

        // 1. 获取字符串长度
        System.out.println(s.length());

        // 2. 根据index提取字符串中的字符
        char c = s.charAt(3);
        System.out.println(c);

        System.out.println("--------------------------------------");

        // 字符串的遍历
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            System.out.println(ch);
        }

        System.out.println("--------------------------------------");

        // 3. 把字符串转换成字符数组
        // 字符串的另一种遍历方法
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            System.out.println(chars[i]);
        }

        System.out.println("---------------------------------------");

        // 4. 判断字符串内容，内容一样就返回true
        String s1 = new String("Chloe");
        String s2 = new String("Chloe");
        System.out.println(s1 == s2); // false, 地址不一样
        System.out.println(s1.equals(s2)); // true

        System.out.println("---------------------------------------");

        // 5. 忽略大小写比较字符串内容，常用来比较验证码
        String c1 = "34AeDF";
        String c2 = "34aEdf";
        System.out.println(c1.equals(c2));
        System.out.println(c1.equalsIgnoreCase(c2));

        System.out.println("----------------------------------------");

        // 6. 截取字符串内容 (输入开始和结束index，包前不包后)
        String s3 = "Java时最好的编程语言之一";
        String rs = s3.substring(0, 8);
        System.out.println(rs);

        System.out.println("-----------------------------------------");

        // 7. 从当前索引位置一直截取到字符串的末尾
        String rs2 = s3.substring(5);
        System.out.println(rs2);

        System.out.println("--------------------------------------");

        // 8. 字符串中的某个内容替换成新的内容，并返回新的字符串对象给我们，常用来替换脏话
        String info = "这个电影简直是个垃圾，垃圾电影！";
        String rs3 = info.replace("垃圾", "**");
        System.out.println(rs3);

        System.out.println("--------------------------------------");

        // 9. 判断字符串中哦是否包含某个关键字
        String info2 = "Java是最好的编程语言之一，我爱Java，Java不爱我!";
        System.out.println(info2.contains("Java"));
        System.out.println(info2.contains("java"));

        System.out.println("--------------------------------------");

        // 10. 判断字符串是否异某个字符串开头
        String rs4 = "王晓萱";
        System.out.println(rs4.startsWith("王晓"));
        System.out.println(rs4.startsWith("王晓2"));

        System.out.println("--------------------------------------");

        // 11. 把字符串按照某个指定内容分割成多个字符串，放到一个字符串数组中返回给我们
        String rs5 = "Henry,Chloe,Michelle,Maria";
        String[] names = rs5.split(",");
        for (int i = 0; i < names.length; i++) {
            System.out.print(names[i]);
        }
    }
}
