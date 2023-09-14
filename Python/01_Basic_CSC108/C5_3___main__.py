"""
1) Purpose: write the code that should only be run when the module is run directly and not when the module is imported
    a) when the code from file is outside of the if __name__ == '__main__', it's executed when being imported
2) Can tell whether it is the main program

"""
# __name__: a special string variable in every module
import C2_2_Define_Function

# When the created variable __name__ is '__main__', this module is the main program.
print('__name__ is', __name__)

# When imports a module, python set the module's __name__ variable to be the name of the module
# rather than the special string '__main__'
print('After import, __name__ is', __name__, 'and C2_2_Function_Definition.__name__ is',
      C2_2_Define_Function.__name__)

