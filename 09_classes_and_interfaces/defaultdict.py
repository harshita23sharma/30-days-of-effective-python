"""
Accept functions instead of classes for simple interfaces.
Python built in apis allow you to customaize behavior by passing in a function.
THese hooks are used by APIs to call back your code while they execute.
For eg. list type sort method takes an optional key argument that's used to determine
each index's value for sorting
Functions work as hooks.
For the same reason defaultdict is preferred over setdefault to handle missing items

"""

def log_missing():
    print("Key added")
    return 0

from collections import defaultdict

from pydata_google_auth import default

current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]

# Supplying function log_missing for determining default values
result = defaultdict(log_missing, current)
print("Before:", dict(result))
for key,amount in increments:
    result[key] += amount
print("After: ", dict(result))

# Now, if I want to count the total number of missing keys
# Using Stateful closure
from collections import defaultdict

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # Stateful Closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

# Supplying function log_missing for determining default values
print("Before:", dict(current))
result, added_count = increment_with_report(current, increments)
for key,amount in increments:
    result[key] += amount
print("After: ", dict(result))
print("added_count: ", added_count)

# Problem with stateful closure is that they are harder to read than the stateless function

# Another way,define a class that encapsulate the state which you want to track

class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added +=1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current) # Method ref

for key, amount in increments:
    result[key] += amount

assert counter.added == 2

# Above, the purpose of CountMissing is unclear, who constructs a CountMissing object?
# Who calls the missing method? Will the class need other public methods to be addded in future?
# Until you see the usage with defaultdict, the class is a mystery

# Hence introducing classmethods