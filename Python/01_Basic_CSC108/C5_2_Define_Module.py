"""
1) The python file is a module.
2) If a module is to be imported by another module, then the files containing the two modules should be saved
 in the same directory or use absolute file paths
3) Python execute modules as it imports them: when there is a print(), python will directly execute.
4) after import, even edit that module's file, and then reimport, the module won't be reloaded
    a) until restart the shell or call imp.reload
"""
from C2_2_Define_Function import calculate_tax
print(calculate_tax(15.0, 90.0))


