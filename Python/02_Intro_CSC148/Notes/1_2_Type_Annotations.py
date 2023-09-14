"""
1) When we want to express more detailed compound types when defining the
function, we need to import the typing module
    a) List[T]: a list whose elements are all type t
    b) Dict[T1, T2]: a dictionary whose key are of type T1 and whose values are
    of type T2
    c) Tuple[T1, T2]: a tuple whose first element has type t1, second element
    has type t2
    e.g. the nested list [[1, 2, 3], [-2]] has type: List[List[int]]

2) Four Advanced Types(also imported from the typing module)
    a) Any: when we want to specify that the type of a value could be anything
    b) Union: when we want to express in a type annotation that a value could be
    one of two different types
    c) Optional: when we want to say a value could be a certain type, or None
        § Optional[T] = Union[T, None]
    d) Callable: when we wnat to express that the type of a parameter, return
    value, or instance attribute is itself a function
        § Takes two expressions in square brackets
        § first: a list of types, representing the types of the function's
        arguments
        § second: its return type
        e.g. Callable[[int, str], bool]: a type expression for a function that
        takes two arguments, an integer and a string, and returns a boolean.
"""
from typing import List, Tuple, Dict, Any, Union, Optional, Callable

# --------------- Annotating Values in Function ---------------
def split_num(num: List[int]) -> Tuple[List[int], List[int]]:
    pass

# --------------- Annotating Instance Attributes ---------------
class Inventory:
    """
    """
    size: int
    items: Dict[int, Tuple[str, int]]
    pass

# --------------- Four Advanced Types ---------------
# Any
def get_first(items: list) -> Any:
    pass

# Union
def cube_root(x: Union[int, float]) -> float:
    pass

# Optional
def find_pos(numbers: List[int]) -> Optional[int]:
    pass

# Callable
def compare_num(num1: int, num2: int, comp: Callable[[int, int], bool]) -> int:
    pass
