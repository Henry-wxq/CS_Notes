"""
1) Private Attribute: with a leading underscore
    a) want the client code programmer writer know that they should not access
    the instance variable

2) Superclass(base class, parent class) and Subclass(derived class, child class)
    a) if an object is an instance of subclass, then it's also and instance of
    its superclass. Therefore, it can get access to all method in superclass.
        >>> fred = SalariedEmployee()
        >>> isinstance(fred, SalariedEmployee)
        True
        >>> isinstance(fred, Employee)
        True
        >>> fred.get_monthly_payment()
    b) when we define the method orginally in the superclass in subclass again,
    this new method definition overrides the inherited definition.
        >>> fred = SalariedEmployee()
        >>> fred.get_monthly_payment()
        5000.0
        >>> jerry = HourlyEmployee()
        >>> jerry.get_monthly_payment()
        3200.0
    c) Method Resolution(when code calls a.myMethod())
        § Python determines what type(a) is and looks in that class for myMethod
        § If myMethod is found in this class, that method is called
        § otherwise, Python next searches for myMethod in the supperclass of the
        type of a, and then the superclass of the supperclass until it either
        finds a definitino of myMethod
        § If it has exhausted all possibilities, it raises an AttributeError
    d) initializer in a subclass
        § Because the initializer is a method, it's inherited by subclasses
        (even the private attribute)
        § however, a superclass initializer is not caleed automatically when a
        subclass instance is created; when the subclass initializer explicitly
        calls the superclass initializer, which initializes the attributes

3) Abstract Method: change the body of the incomplete method so that it raises a
NotImplementedError
    a) we call a class which has at least one abstract method an abstract class
"""
from typing import List
from datetime import date


class Employee:
    """An employee of a company

    """
    def __init__(self, id_: int, name: str) -> None:
        """Initialize this employee
        """
        self.id_ = id_
        self.name = name

    # it has to be different for each type of employee. The subclass will
    # inherit this uncomplete method and redefine as appropriate.
    def get_monthly_payment(self) -> float:
        """Return the amount that his Employee should be paid in one month.

        round the amount to the nearest cent.
        """
        raise NotImplementedError

    def pay(self, pay_date: date) -> None:
        """Pay this Employee on the gien date and record the payment.

        (Assure called once per month)
        """
        payment = self.get_monthly_payment()
        print(f'An employee was paid {payment} on {pay_date}')


class SalariedEmployee(Employee):
    """
    === Attributes ===
    salary: This employee's annual salary
    # others are inherited from superclass no need to mention

    === Representation Invariants ===
    - salary >= 0
    """
    id_: int
    name: str
    salary: float

    def __init__(self, id_: int, name: str, salary: float) -> None:
        """Initialize SalariedEmployee
        # use Employee.__init__(self, id_, name) as helper method
        """
        Employee.__init__(self, id_, name)
        self.salary = salary

    def get_monthly_payment(self) -> float:
        # Assuming an annual salary of 60, 000
        return round(60000.0 / 12.0, 2)

    def pay(self, pay_date: date) -> None:
        # Override an implemented method to extend it
        Employee.pay(self, pay_date)  # call the superclass method as a helper
        print('Payment accepted! Have a nice day. :)')


class HourlyEmployee(Employee):
    """

    """



if __name__ == '__main__':
    a = SalariedEmployee(1, 'Henry', 10.0)
