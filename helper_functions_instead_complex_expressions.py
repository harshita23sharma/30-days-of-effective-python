def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default


def run():
    my_values = {"red": ["5"], "blue": ["0"], "green": [""]}
    red = my_values.get("red", [""])
    print(f"red: {red}")  # Returns red: ['5']

    red = my_values.get("red", [""])[0]
    print(f"red: {red}")  # Returns red: 5

    red = my_values.get("red", [""])[0]
    # Below, !r is equivalent to str.format()
    print(f"red: {red!r}")  # Returns red: '5'

    # If key is not present, default [""] is returned
    violet = my_values.get("violet", [""])[0]
    print(f"violet: {violet}")  # Returns violet:

    # Above statement returns empty string,
    # Empty string, empty list and  zero all evaluate to False implicitly
    violet = my_values.get("violet", [""])[0] or 0
    print(f"violet: {violet!r}")  # Returns violet: 0

    red_before = int(my_values.get("red", [""])[0] or 0)
    # Above line has become hard to read post int()

    # Better way is to use if/else for better readability
    red_str = my_values.get("red", [""])
    red_after = int(red_str[0]) if red_str[0] else 0

    assert red_before == red_after  # No error

    # If we are reusing the same logic multiple times for green etc,
    # better to use helper function
    green = get_first_int(my_values, "green")
    print(f"green: {green}")  # return green: 0


if __name__ == "__main__":
    run()
