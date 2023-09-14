"""
1) __str__: caleed when call either str or print on an object
2) __eq__: whose default implementation simply uses to compare two objects.
"""


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


cat_1 = Item('Cat', 5)
cat_2 = Item('Cat', 5)

print(cat_1 == cat_2)
# False, because id is not the same, should be True
print(cat_1)
# <__main__.Item object at --->


class Item2:
    def __init__(self, name, weight):
        self.name=name
        self.weight=weight

    def __eq__(self, other):
        # `__eq__` is an instance method, which also accepts
        # one other object as an argument.

        if type(other) == type(self) and other.name == self.name and\
                other.weight == self.weight:
            return True
        else:
            return False  # 返回False这一步也是需要写的哈，不然判断失败就没有返回值了

    def __str__(self):
        return 'The name of this cat is {}'.format(self.name)


cat_3 = Item2('Cat', 5)
cat_4 = Item2('Cat', 5)

print(cat_3.__eq__(cat_4))  # should evaluate to True
print(cat_3 == cat_4)  # should also evaluate to True

print(cat_3)
print(cat_4)
# The name of this cat is Cat
# The name of this cat is Cat



