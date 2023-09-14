"""
1) Abstract Data Type: defines some kind of data and the operations that can
be performed on it.
    a) A pure interface, with no mention of an implementation
    b) About:
        § What data is stored
        § What we can do with this data

2) Data Structure(contrast to ADT): a concrete strategy for storing some data.
    a) About:
        § How is that data stored
        § How do we actually implement our desired methods to operate on this
        data

3) ADT Types:
    a) Set
        § Data: a collection of unique elements
        § Operations: get size, insert a value (without introducing duplicates),
        remove a specified value, check membership
    b) Multiset
        § Data: a collection of elements (possibly with duplicates)
        § Operations: same as Set, but the insert operation allows duplicates
    c) List
        § Data: an ordered sequence of elements
        § Operations: access element by index, insert a value at a given index,
        remove a value at a given index
    d) Map
        § Data: a collection of ey-value pairs, where each key is unique and
        associated with a single value
        § Operations: lookup a value for a given key, insert a new key-value
        pair, remove a key-value pair, update the value associated with a give
        key
    e) Iterable
        § Data: a collection of values (may or may not be unique)
        § Operations: iterable through the elements of the collection one at a
        time

4) Some reminder
    a) Difference between Python's built-in classes and the ADTs we've listed
    above:(there is not a one-to-one correspondence between ADTs and data
    structure)
        § list and dict are data structures, not ADTs
        § a dict, is not itself an ADT but it's a natural implementation of the
        Map ADT
    b) a single ADT can be implemented by many different daya structures
    c) each data structure can be used to implement multiple ADTs
"""
