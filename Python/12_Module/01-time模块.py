import time
# time模块的时间戳是time.time()
# the second is counted from 1970.1.1
# the end is depends on different system
a = time.time()
print(a)

# time tuple1: time.localtime(time.time())
# means: 从时间戳转换到现在的时间，元祖中有9个数据
# time tuple2: time.gmtime(time.time())
# means: 从时间戳转换到现在的伦敦时间
# tm_year：现在的年份；tm_mon：现在的月份; tm_mday：现在的日期; tm_hour：现在的小时;
# tm_min：现在的分钟; tm_sec：现在的秒数; tm_wday：现在的星期(0-7); tm_yday：现在是今年的第多少天(0-366);
# tm_isdst：夏令时是否生效（-1:未知；0:不生效；1:生效）
b = time.localtime(time.time())
c = time.gmtime(time.time())
print(b)
print(c)

# time.asctime(time tuple)转换成人话
d = time.asctime(b)
print(d)

# time.mktime(time tuple)转换成时间戳
e = time.mktime(b)
print(e)

# time.sleep(秒数)
# 线程睡眠的秒数
import threading


def drink():
    for i in range(6):
        print("-----在喝茶-----")
        time.sleep(1)


def sing():
    for i in range(6):
        print("-----在唱歌-----")
        time.sleep(1)


def main():
    ti = threading.Thread(target=drink)
    t2 = threading.Thread(target=sing)
    ti.start()
    t2.start()

if __name__ == '__main__':
    main()
