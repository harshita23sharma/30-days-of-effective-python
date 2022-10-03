"""
In Python3.5, the order of iteration would not match the order in which the items were inserted.

Don't assume that insertion ordering behaviour will be present when you're handling dictionaries.

Python makes it easier for programmer to define their own custom container types
that emulate the standard protocols mtching list, dict and other types
"""

# function to process the voting data and save the rank in provided empty dict
def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


# funct telling which animal won the contest
def get_winner(ranks):
    return next(iter(ranks))


"""
Requirement 2: Should be in alphabetical order
Using collections.abc built in class to define a new dictionary-like
class that iterates its contents in alphabetical order
"""

from collections.abc import MutableMapping


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


def get_winner_new(ranks):
    if not isinstance(ranks, dict):
        raise TypeError("must provide a dict instance", type(ranks))
    return next(iter(ranks))


def run():
    # Show the result of te contest for cutest baby animal
    votes = {
        "otter": 1281,
        "polar bear": 587,
        "fox": 863,
    }
    ranks = {}
    populate_ranks(votes, ranks)
    print(ranks)  # Returns: {'otter': 1, 'fox': 2, 'polar bear': 3}

    # I can use SortedDict instance in place of  standard dict
    votes = {
        "otter": 1281,
        "polar bear": 587,
        "fox": 863,
    }
    sorted_ranks = SortedDict()
    populate_ranks(votes, sorted_ranks)
    print(sorted_ranks.data)  # Returns {'otter': 1, 'fox': 2, 'polar bear': 3}
    winner = get_winner(sorted_ranks)
    print(winner)  # Returns fox instead of otter
    # The problem here is get_winner assumes that the dictionary's iteration
    # is in the insertion order to match populate_ranks. The code is using
    # SortedDIct instead of dict, so that assumption is no longer true.
    # Thus the value returned for the winner is "fox", which is alphabetically first.

    print(
        get_winner_new(sorted_ranks)
    )  # Raises exception TypeError: ('must provide a dict instance', <class '__main__.SortedDict'>)

    


if __name__ == "__main__":
    run()
