"""
1) class: a block of code that defines a type of data
(Suppose we have a class called X)
    a) instance attributes (data)
    b) methods (operations)
    c) representation invariants (properties)

2) Instance: An object whose type is X is called an instance of class X
    e.g. the object 3 is an instance of class int
    a) may not only just a single piece of data
    b) can hold a collection of data bundled together
    c) instance attribute(attribute): each individual piece of data in an
    instance

3) initializer: called automatically to create and initialize the instance
attributes

4） representation invariant: a property of the instance attributes that every
instance of a class must satisfy
    a) Document representation invariants: in the docstring of a class,
    underneath its attributes
        § in english
        § concrete Python code expressions that evaluate to True or False
        § every instance attribute type annotation is a representation invariant
    b) Enforcing representation invariants: both a precondition and
    postcondition of every method in a class
    c) For initializer: it doesn't have any preconditions on the attribute but
    it must initialize the attributes so that they satisfy every representation
    invariant
"""
from datetime import date
from typing import List


class Tweet:
    """Description
    === Attributes ===
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    content: the contents of the tweet.
    likes: the number of likes this tweet has received.

    === Representation Invariants ===
    - len(self.content) <= 280
    """
    # attribute types
    userid: str
    created_at: date
    content: str
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a Tweet

        # representation invariants
        Precondition: len(what) <= 280.
        """
        pass


# compound class
class User:
    """A Twitter user.

    === Attributes ===
    userid: the userid of this Twitter user.
    bio: the bio of this Twitter user.
    tweets: the tweets that this user has made.

    """
    # Attribute types
    userid: str
    bio: str
    tweets: List[Tweet]

    def __init__(self):
        pass
