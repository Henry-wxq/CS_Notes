package com.henryw.junitdemo1;

import org.junit.Assert;
import org.junit.Test;

/**
 * 测试类
 */

public class StringUtilTest {
    @Test
    public void testPrintNumber() {
        StringUtil.printNumber("Henry");
        StringUtil.printNumber(null);
    }

    @Test
    public void testGetMaxIndex() {
        int maxIndex = StringUtil.getMaxIndex(null);
        System.out.println(maxIndex);

        int maxIndex2 = StringUtil.getMaxIndex("Henry");
        System.out.println(maxIndex2);

        // 断言机制
        // 期望值是-1，实际值是5，测试失败
        Assert.assertEquals("有问题", 4, maxIndex2);
    }
}
