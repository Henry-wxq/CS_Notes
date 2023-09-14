"""
1) id: the id of an object is a unique identifier
    a) the memory address doesn't have to be the id of the object; just need to
    guarantee uniqueness

2) type: type determines what functions can operate on it

3) variable: not an object; stores an id that refers to an object that stores
data.
    a) variable itself has no type; python reports the type of the object that
    variable refers to
        § it's different from many other languages, such as Java and C, where
        every variable has a type

4) Executing an assignment statement(always has an expression on the right-hand
side)
    a) Evaluate the expression on the right-hand side, yielding the id of an
    object
    b) If the variable on the left-hand-side doesn't already exist, create it.
    c) Store the if from the expressino on the right-hand-side in the variable
    on the left-hand-side

5) Mutability
    a) Immutable: the value stored in an object of that type can't change (any
    new object has a different id)
    b) Mutable: any method or operations applied on the value doesn't change its
    id (even change its size)

6) Aliasing: when two variables refer to the same object, the variables are
aliases of each other.

7) Side Effect: when two variable are referring to a mutable object(aliasing to
each other), mutate any one of the variables will change the other variable
    a) when the variables referring is immutable, it's still aliasing but
    immutable values can never be changed; therefore, a typeerror exists.

8) Reference: my_var = ...... ever mutates the object that my_var refers to
previously; it sets my_var to refer to a different object

9) Equality
    a) Value Equality: use '==' operator to compare the values stored in the
    objects they reference
    b) Identity Equality: use 'is' operator to compare the ids of the objects
    they reference
"""
# ------------------------------ aliasing ------------------------------
# z = x: make z refer to the object that x refer to
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(id(x))
print(id(y))
print(id(z))

# for mutable data type (side effect)
z[0] = 999
print(x)

# ------------------------- reference and mutate -------------------------
# Instead of mutating the object that z refers to, we make z refer to a new
# object; no effect on the object that x refers to
a = [1, 2, 3]
b = a
b = [1, 2, 3, 4]
print(a)

# ------------------------------ equality ------------------------------
e = [1, 2, 3]
f = [1, 2, 3]
print(e == f)
print(e is f)

# special case with immutable objects
# when the object is simple and small, then '==' and 'is' are in same boolean
# value
g = 'foo'
h = 'foo'
print(g == h)
print(g is h)

# when it goes to longer and more complex one, then it depends
i = 'asdfasljdhflaksjdhfd;lfkjadkfjak;lsdjflkajkls;df'
j = 'asdfasljdhflaksjdhfd;lfkjadkfjak;lsdjflkajkls;df'
print(i == j)
print(i is j)
