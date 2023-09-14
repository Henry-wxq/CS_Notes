class Machine:
    pass

class Calculator(Machine):
    pass

class FourFunctionCalculator(Calculator):
    pass

if __name__ == '__main__':
    m = Machine()
    c = Calculator()
    f = FourFunctionCalculator()
    print(type(f) == type(c))
