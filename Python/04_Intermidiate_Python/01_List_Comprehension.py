"""
List Comprehension: Works for Sequences
new_list = [new_item for item in list]

Python Sequences: have specific order
- List
- Range
- Tuple
- String

Conditional List Comprehension
new_list = [new_item for item in list if test]
"""

if __name__ == "__main__":
    # Example 1: List
    numbers = [1, 2, 3]

    # new_list = []
    # for n in numbers:
    #     add_1 = n + 1
    #     new_list.append(add_1)
    new_list_1 = [n + 1 for n in numbers]
    print(new_list_1)

    # Example 2: Strings (Other sequences)
    name = "Henry"
    new_list_2 = [n for n in name]
    print(new_list_2)

    # Example 3: Range
    new_list_3 = [n * 2 for n in range(1, 5)]
    print(new_list_3)

    # Conditional List Comprehension
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    short_names = [name for name in names if len(name) < 5]
