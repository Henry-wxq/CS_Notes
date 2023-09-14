# function can be passes as an argument as well
def function_runner(f: "callable"):
    """Call f.

    """
    f()


def function_1():
    """Print that this function was called
    """
    print('function_1 was called')


if __name__ == '__main__':
    function_runner(function_1())