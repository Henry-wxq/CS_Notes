package com.henryw.mapdemo2;

import java.util.HashMap;
import java.util.Map;

/**
 * Map的常用方法
 *
 */

public class Test {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 2);
        map.put("c", 4);
        map.put("c", 3); // key重复，value覆盖
        map.put(null, null);
        System.out.println(map); // {null=null, a=1, b=2, c=3}

        // 1. int size(): 返回map中键值对的个数
        System.out.println(map.size()); // 4

        // 2. void clear(): 清空map
//        map.clear();
//        System.out.println(map); // {}

        // 3. boolean isEmpty(): 判断map是否为空
//        System.out.println(map.isEmpty()); // true

        // 4. V get(Object key): 根据key获取value
        System.out.println(map.get("a")); // 1

        // 5. V remove(Object key): 根据key删除键值对, 返回被删除的value
//        System.out.println(map.remove("a")); // 1

        // 6. boolean containsKey(Object key): 判断map中是否包含指定的key, 包含返回true, 不包含返回false
        System.out.println(map.containsKey("a")); // true

        // 7. boolean containsValue(Object value): 判断map中是否包含指定的value, 包含返回true, 不包含返回false
        System.out.println(map.containsValue(1)); // true

        // 8. Set<K> keySet(): 获取map中所有的key, 返回一个Set集合
        System.out.println(map.keySet()); // [null, a, b, c]

        // 9. Collection<V> values(): 获取map中所有的value, 返回一个Collection集合
        System.out.println(map.values()); // [null, 1, 2, 3]

        // 10. 把其它Map中的所有键值对都添加到当前Map中
        Map<String, Integer> map2 = new HashMap<>();
        map2.put("d", 4);
        map2.put("e", 5);
        Map<String, Integer> map3 = new HashMap<>();
        map2.put("d", 100);
        map2.put("f", 500);
        map2.putAll(map3); // 把map3中的所有键值对都添加到map2中
        System.out.println(map2); // {d=100, e=5, f=500}
    }
}
