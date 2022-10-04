"""
Prefer get Over in and Keyerror to Handle Missing Dictionary Keys

The get method is best for dictionaries that contain basic types
like counters, and it is preferable along with assignment expressions
when creating dictionary values have high cost or may raise exceptions
"""


def run():
    votes = {"baguetta": ["Bob", "Alice"], "ciabatta": ["Coco", "Deb"]}
    key = "brioche"
    who = "Elmer"

    """
    Way 1: IN expression
    """
    if key in votes:
        names = votes[key]
    else:
        votes[key] = names = []
    names.append(who)
    print(votes)

    """
    Way 2: KeyError expression
    """
    try:
        names = votes[key]
    except KeyError:
        votes[key] = names = []

    names.append(who)

    """Best Way: GET method"""

    names = votes.get(key)
    if names is None:
        votes[key] = names = []

    names.append(who)

    """ Further shortened way"""

    if (names := votes.get(key)) is None:
        votes[key] = names = []
    names.append(who)

    """Another Way : SETDEFAULT method"""
    names = votes.setdefault(key, [])
    names.append(who)

    """ 
    The default value passed o setdefault is assigned directly into the dictionary
    when the key is missing instead of being copied.
    """
    data = {}
    key = "foo"
    value = []
    data.setdefault(key, value)
    print("Before", data)
    value.append("hello")
    print("After: ", data)


if __name__ == "__main__":
    run()
