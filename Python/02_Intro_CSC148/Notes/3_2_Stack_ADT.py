"""
1) Stack ADT: last in first out (LIFO)
    a) Data: a collection of items
    b) Operations:
        § determine whether the stack is empty
        § add an item(push)
        § remove the most recently-added item(pop)
    c) Reminders
        § Picturing implementation with a Python list is irrelevant when using
        the ADT
        § when being a client, don't need to know the implementation

2) Queue ADT: first in first out (FIFO)
    a) Data: a collection of items
    b) Operations:
        § determine whether the queue is empty
        § add an item(enqueue)
        § remove the least recently-added item(dequeue)

3) Raise a user-defined exception: when don't want to fail silently
    a) let the errors to be descriptive
    b) Method: define our own ty[e of error by making a subclass of a built-in
    class called Exception
    c) when raising it, just this simple raise statement will reveal, it doesn't
    mention any implementation details of the class
    d) when an exception is raised, the functino ends and its frame ends
    immediately

4) try...except...(else...finally) exceptions:
def xxx(x):
    try:
        可能出现异常的代码
    except (Error1, Error2, Error3, ...) as e:  # 一个except可同时处理多个
        处理异常的代码
    except [Exception]:  # 可以有多个except，通常在最后一个except中使用[Exception]
    # [Exception]为所有异常类型
        处理异常的代码
    else:
        当try中代码没问题时会调用else中的代码， 前面必须有except
    finally:
        不管try代码是否正常，最终都会调用finally中的代码

5) Analysing Program Running Time
    a) use built-in library called: timeit
"""
from typing import List, Any, Optional


class Stack:
    """A LIFO stack of tiems

    === Private Attributes ===
    _items: the items stored in the stack. The end of the list represents the
    top of the stack

    """
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty stack.
        """
        self._items = []

    def is_empty(self) -> bool:
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remover and return the element at the top of this tack
        """
        if not self.is_empty():
            return self._items.pop()
        else:
            raise EmptyStackError


class EmptyStackError(Exception):
    """Exception raised when calling pop on an empty stack."""
    # Overriding the inherited __str__ method in the subclass
    def __str__(self) -> str:
        """Return a string representation of this error"""
        return 'You called pop on an empty stack. :('


# Alternatively, we can do this in a more elegant way when using try...except
def second_from_top(s: Stack) -> Optional[str]:
    """Return a reference to the item that is second from the top of s.
    Do not change s.

    If there is no such item in the Stack, returns None.
    """
    hold2 = None
    try:
        # Pop and remember the top 2 items in s.
        hold1 = s.pop()
        hold2 = s.pop()
        # Push them back so that s is exactly as it was.
        s.push(hold2)
        s.push(hold1)
        # Return a reference to the item that was second from the top
    except EmptyStackError:
        print("Cannot return second from top, stack empty")
    return hold2


if __name__ == '__main__':
    s = Stack()
    s.pop()
