"""
1) if <<condition>>:
       <<if_block>>
   elif <<condition>>:
       <<elif_block>>
   else:
       <<else_block>>
    a) condition is an expression; doesn't have to be a Bool expression, non-bool values are treated as True or
     False when required
    b) block of statements in an if must be indented.
    c) if two conditions are related, use elif clause instead of two ifs
    d) An if statement can have at most one else clause
    e) no condition associated with else; below are logically equivalent
        § else:
            <<else_block>>
        § if not <<condition>>:
            <<else_block>>
2) nested: an if statement inside another
"""
