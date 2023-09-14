"""
1)
"""
# Linear Search: find an item in an unsorted list; find the leftmost one if duplicated
# Starts at index 0 an looks at each item one by one
def linear_search(lst: list, v: object) -> int:
    """Return the index of the first occurrence of v in L, or return -1 if
    v is not in L.

    >>>
    """
    i = 0

    while i != len(lst) and v != lst[i]:
        i += 1

    if i == len(lst):
        return -1
    else:
        return i

# Binary Search: find an item in a sorted list
def binary_search(lst: list, v: object) -> int:
    """Return the index of the first occurrence of v in L, or return -1 if
    v is not in L.

    Precondition1: lst is sorted from smallest to largest
    Precondition2: all the items in L can be compared to v

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 5], 5)
    2
    >>> binary_search([2, 3, 5, 7], 8)
    -1
    """
    b = 0
    e = len(lst) - 1

    while b <= e:
        m = (b + e) // 2

        if lst[m] < v:
            b = m + 1
        else:
            e = m + 1

    if b == len(lst) or lst[b] != v:
        return -1
    else:
        return b

