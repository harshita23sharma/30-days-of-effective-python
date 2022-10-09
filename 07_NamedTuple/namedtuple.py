"""
namedtuple() : The factory function

    Are immutable data structures
    Have a consistent hash value
    Can work as dictionary keys
    Can be stored in sets
    Have a helpful docstring based on the type and field names
    Provide a helpful string representation that prints the tuple content in a name=value format
    Support indexing
    Provide additional methods and attributes, such as ._make(), _asdict(), ._fields, and so on
    Are backward compatible with regular tuples
    Have similar memory consumption to regular tuples

In general, you can use namedtuple instances wherever you need a tuple-like object. Named tuples have the advantage that they provide a way to access their values using field names and the dot notation.



"""
from collections import namedtuple
from datetime import date

"""
To create a new namedtuple, you need to provide two positional arguments to the function:

    typename provides the class name for the namedtuple returned by namedtuple(). You need to pass a string with a valid Python identifier to this argument.
    field_names provides the field names that you’ll use to access the values in the tuple. You can provide the field names using:
        An iterable of strings, such as ["field1", "field2", ..., "fieldN"]
        A string with each field name separated by whitespace, such as "field1 field2 ... fieldN"
        A string with each field name separated by commas, such as "field1, field2, ..., fieldN"

"""
## Subclassing namedtuple Classes
BasePerson = namedtuple("BasePerson", "name birthdate country", defaults=["Canada"])


class Person(BasePerson):
    """A namedtuple subclass to hold a person's data."""

    __slots__ = ()  # ref: https://docs.python.org/3/reference/datamodel.html#object.__slots__

    def __repr__(self):
        return f"Name: {self.name}, age: {self.age} years old."

    @property
    def age(self):
        return (date.today() - self.birthdate).days // 365


def run():
    Point = namedtuple("Point", ["x", "y"])
    Point = namedtuple("Point", (field for field in "xy"))
    Point(8, 16)  # Returns Point(x=8, y=16)
    # Converting namedtuple Instances Into Dictionaries
    Person = namedtuple("Person", "name age height")
    jane = Person("Jane", 25, 1.75)
    jane._asdict()  # returns {'name': 'Jane', 'age': 25, 'height': 1.75}
    # Since Python 3.8, ._asdict() has returned a regular dictionary. Before that, it returned an OrderedDict object

    jane = jane._replace(age=26)
    # Person(name='Jane', age=26, height=1.75)
    # Person.__doc__
    # A namedtuple subclass to hold a person's data."
    # jane = Person("Jane", date(1996, 3, 5))
    # jane.age #25
    # >>> jane output: Name: Jane, age: 25 years old
    # Person inherits from BasePerson, which is a namedtuple class.
    # In the subclass definition, you first add a docstring to describe what the class does.
    # Then you set __slots__ to an empty tuple, which prevents the automatic creation of a per-instance .__dict__.
    # This keeps your BasePerson subclass memory efficient.


if __name__ == "__main__":
    run()
