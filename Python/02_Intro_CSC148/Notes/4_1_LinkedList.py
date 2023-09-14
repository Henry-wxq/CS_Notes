"""

"""
from typing import Any, Optional


class _Node:
    """

    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """
        """
        self.item = item
        self.next = None


class LinkedList:
    """
    """
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """
        """
        self._first = None
        for item in items:
            self.append(item)

    def print_items(self) -> None:
        """
        """
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def to_list(self) -> list:
        """
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(curr.item)
            curr = curr.next
        return items

    def append(self, item: Any) -> None:
        """
        """
        curr = self._first
        if curr is None:
            new_node = _Node(item)
            self._first = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            new_node = _Node(item)
            curr.next = new_node

    def insert(self, index: int, item: Any) -> None:
        """
        """
        curr = self._first
        curr_index = 0

        while curr is not None and curr_index < index - 1:
            curr = curr.next
            curr_index += 1

        if curr is None:
            raise IndexError
        else:
            new_node = _Node(item)
            new_node.next = curr.next
            curr.next = new_node

