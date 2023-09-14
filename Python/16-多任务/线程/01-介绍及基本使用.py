"""多任务：同时跑多个程序"""
import time
import threading


def sing():
    """sing for 5s"""
    """time.sleep(): 线程休眠的秒数"""
    for i in range(5):
        print("-----zxq猪猪-----")
        time.sleep(1)

def dance():
    """dance for 5s"""
    for i in range(5):
        print("-----wxq牵猪-----")
        time.sleep(1)

def main():
    """注意此处sing和dance后面没有括号"""
    a = threading.Thread(target=sing)
    b = threading.Thread(target=dance)
    a.start()
    b.start()


if __name__ == "__main__":
    main()