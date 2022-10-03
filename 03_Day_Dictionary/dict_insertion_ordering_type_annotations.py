"""
Using type annotations to enforce that the value passed to get_winner is 
a dict instance and not a MutableMapping with dictionary-like behavior
"""
from typing import Dict, MutableMapping

# function to process the voting data and save the rank in provided empty dict
def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


# funct telling which animal won the contest
def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


"""
Requirement 2: Should be in alphabetical order
Using collections.abc built in class to define a new dictionary-like
class that iterates its contents in alphabetical order
"""


class SortedDict(MutableMapping[str, int]):
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

    sorted_ranks = SortedDict()
    populate_ranks(votes, sorted_ranks)
    print(sorted_ranks.data)  # Returns {'otter': 1, 'fox': 2, 'polar bear': 3}
    winner = get_winner(sorted_ranks)
    print(
        winner
    )  # Running python3 -m mypy --strict dict_insertion_ordering_type_annotations.py
    # Returns dict_insertion_ordering_type_annotations.py:67: error: Argument 1 to "get_winner" has incompatible type "SortedDict"; expected "Dict[str, int]"
    # dict_insertion_ordering_type_annotations.py:72: error: Call to untyped function "run" in typed context


if __name__ == "__main__":
    """
    There are three ways to be carefule about dictionaries-like classes:
    Write code that doesn't rely on insertion ordering,
    explicitly check for the dict type at runtime,
    or require dict values using type annotations and static analysis
    """
    run()
