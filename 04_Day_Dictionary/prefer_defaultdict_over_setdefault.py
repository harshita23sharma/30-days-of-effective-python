"""
Setdefault is only shortest way to handle missing dictionary keys, when the default values are 
cheap to construct, mutable and there is no potential for raising exceptions (e.g. list instances)
like list
NOTE: Setdefault method of dict is a bad fit when creating the default value has 
high computational cost or may raise exception
Prefer defaultdict over setdefault to handle missing items in Internal State

NOTE: The function passed to defaultdict must not require any arguments,
which makes it impossible to have the default value depend on the key being accessed
"""

# CASE 1 : When you are given a dictionary
### eg: keep track of cities visited in a country (key), where cities are in set as values
def run():
    visits = {"Mexico": {"Tulum", "Puerto Vallarta"}, "Japan": {"Hakone"}}
    # Shorter approach using setdefault
    visits.setdefault("France", set()).add("Arles")

    # Longer way using get method
    if (japan := visits.get("Japan")) is None:
        visits["Japan"] = japan = set()
    japan.add("Kyoto")
    print(visits)


# CASE 2 : When you are not given a dictionary but you control the creation
# You control dictionary accessing and keeping track of the internal state of a class


class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


# THis new class hides the complexity of calling setdefault correctly
# setdefault is a confusing name
# Bigger Drawback is setdefault is comutation inefficient bcoz it constructs
# a new set instance on every call, regardless of whether the given country was
# already present in the data dictionary

# Solution : defaultdict automatically stores a default value when a key doesn't exist.
# All we need is to provide a function that will return the default value to use each time
# a key is missing

from collections import defaultdict


class Visits2:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


# In above case, No superfluous set instance will be allocated, which could be costly if add
# method is called a large number of times.

if __name__ == "__main__":
    run()
    visits1 = Visits()
    visits1.add("England", "Bath")
    visits1.add("England", "London")
    print(visits1.data)
    visits2 = Visits2()
    visits2.add("England", "Bath1")
    visits2.add("England", "London1")
    print(visits2.data)
