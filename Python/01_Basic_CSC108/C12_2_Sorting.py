"""

"""
# ---------------------------------------- Bubble Sort ----------------------------------------
def bubble_sort(lst: list) -> None:
    """ Sort the items of L from smallest to largest

    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    # The index of the last unsorted item
    end = len(lst) - 1

    while end != 0:
        # bubble once through the unsorted section to move the
        # largest item to index end
        for i in range(end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

        end -= 1

# ---------------------------------------- Selection Sort ----------------------------------------
def get_index_of_smallest(lst: list, i: int) -> int:
    """ Return the index of the smallest item in lst[i:]

    >>> get_index_of_smallest([2, 7, 3, 5], 1)
    2
    """
    # The index of the smallest item so far
    index_of_smallest = i

    for k in range(i + 1, len(lst)):
        if lst[k] < lst[index_of_smallest]:
            index_of_smallest = k

    return index_of_smallest

def selection_sort(lst: list) -> None:
    """ Sort the items of L into non-descnding order

    >>> L = [3, 7, 2, 5]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    for i in range(len(lst)):
        # find the index of the smallest item in lst[i:] and swap that
        # item with the item at index i
        index_of_smallest = get_index_of_smallest(lst, i)
        lst[index_of_smallest], lst[i] = lst[i], lst[index_of_smallest]

# ---------------------------------------- Insertion Sort ----------------------------------------
def insert(lst: list, i: int) -> None:
    """ Precondition: lst[:i] is sorted from smallest to largest

    Move lst[i] to where it belongs in lst[:i+1]

    >>> lst = [7, 3, 5, 2]
    >>> insert(lst, 1)
    >>> lst
    [3, 7, 5, 2]
    """
    # The value to be inserted into the sorted part of the list
    value = lst[i]

    # find the index, j, where the value belongs
    # make room for the value by shifting
    j = i
    while j != 0 and lst[j - 1] > value:
        # shift lst[j - 1] one position to the right to lst[j]
        lst[j] = lst[j - 1]
        j -= 1

    # put the value where it belongs
    lst[j] = value


def insertion_sort(lst: list) -> None:
    """ Sort the item of L from smallest to largest

    >>> L = [7, 3, 5, 2]
    >>> insertion_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    for i in range(len(lst)):
        insert(lst, i)
