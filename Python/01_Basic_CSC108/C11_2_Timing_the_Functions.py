"""
1) Profiling a program: measuring how long it takes to run and how much memory it uses.
"""
# contains functions related to time
import time


# perf_counter(): returns a time in seconds
# call it before and after the code we want to time and take the difference to find out how many second have elapsed

def find_two_min1(lst: list) -> tuple:
    temp_list = sorted(lst)
    min1 = temp_list[0]
    min2 = temp_list[1]
    min1_index = lst.index(min1)
    min2_index = lst.index(min2)
    return (min1_index, min2_index)


def find_two_min2(lst: list) -> tuple:
    if lst[0] < lst[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    for i in range(2, len(lst)):
        if lst[i] < lst[min1]:
            min2 = min1
            min1 = i
        elif lst[i] < lst[min2]:
            min2 = i
    return (min1, min2)


def find_time(func, lst):
    t1 = time.perf_counter()
    func(lst)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000000


data = [324, 576, 890, 123, 23, 54, 634]


if __name__ == '__main__':
    t1 = find_time(find_two_min1, data)
    t2 = find_time(find_two_min2, data)

    print('Sort method took {:.2f}us'.format(t1))
    print('Walk through took {:.2f}us'.format(t2))
