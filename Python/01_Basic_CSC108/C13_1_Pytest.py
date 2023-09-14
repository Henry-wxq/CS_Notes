"""
Choosing Test Cases

1) Size: (for collections such as list, tuple, dictionary)
    a) test with an empty collection
    b) a collection with 1 item
    c) the smallest interesting case
    d) a collection with several items

2) Dichotomies:
    a) vowels/non-vowels
    b) even/odd
    c) positive/negative
    d) empty/full
    ......

3) Boundaries: If the function behaves differently for values near a particular threshold, test at that threshold.

4) Order: If a function behaves differently when the values are indifferent orders identify and test each of
 those orders.

# def calculate_tax(bill: float, tax_rate: float) -> float:  # Function header: names to make easy for readers
#     # expected two empty lines above the function header
#     # two spaces before inline comments
#     # Type Contract: Being involved in the function header, this one, (float, float) -> float
#     # Description: Start with the word 'Return'; mention every parameter in the description and
#     # describe the return value.
#     # Example calls and return values as we would expect to see in the Python Shell.
#
#     Return the amount of tax due on a bill calculated at tex_rate.
#
#     Precondition: 0.0 <= tax_rate <= 1.0
#
#     >>> calculate_tax(10.5, 0.2)
#     2.1
#     >>> calculate_tax(2000.0, 0.0)
#     0.0
#
#
#     return bill * tax_rate  # the body of the function
"""
from C2_2_Define_Function import calculate_tax


# pytest must begin with: test_
def test_no_bill():
    # docsting begin with test
    """Test that bill with 0 amount produces 0 after the function calculate_tax is operated"""

    assert calculate_tax(0.0, 0.5) == 0.0

def test_no_tax():
    """Test that tax with 0% required produces 0 after the function calculated_tax is operated"""

    assert calculate_tax(10.0, 0.0) == 0.0

def test_full_tax():
    """Test that tax with 100% required produces the 2 times the bill amount after the function
    calculated_tax is operated
    """

    assert calculate_tax(10.0, 1.0) == 10.0


def test_normal_tax_bill():
    """Test that tax amd bill amount in a normal condition, 0.5 and 10.5, produces 5.25 after
    the function calculated_tax is operated
    """

    assert calculate_tax(10.5, 0.5) == 5.25


if __name__ == '__main__':
    import pytest
    pytest.main(['C13_1_Pytest.py'])
