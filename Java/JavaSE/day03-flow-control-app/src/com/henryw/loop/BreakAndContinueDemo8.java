package com.henryw.loop;

/**
 * break: 跳出并结束当前所在循环的执行; 只能用于结束所在循环，或者结束所在switch分支的执行
 * countinue：用于跳出当前循环的当此执行，直接进入循环的下一次执行；只能在循环中使用
 */

public class BreakAndContinueDemo8 {
    public static void main(String[] args) {
        // 又有老婆了，你又犯错了，你老婆罚你说5句我爱你，说到第三局的时候心软了，让你别再说了
        for (int i = 1; i <= 5; i++) {
            System.out.println("我爱你");
            if (i == 3) {
                break;
            }
        }

        // 又又有老婆了，你又又犯错了，你老婆罚洗碗，洗到第三天的时候心软了，第四天让你继续洗
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                continue;
            }
            System.out.println("洗碗中" + i);
        }
    }
}
