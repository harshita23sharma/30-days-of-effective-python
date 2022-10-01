"""
Prevent repetiotion with Walrus operator :=
a := b is pronounced as "a walrus b"
"""


def run():
    fresh_fruits = {"apple": 10, "banana": 8, "lemon": 5}

    def make_lemonade(count):
        ...

    def out_of_stock():
        ...

    def make_cider():
        ...

    count = fresh_fruits.get("lemon", 0)
    if count:
        make_lemonade(count)
    else:
        out_of_stock()
    # count is only relevant to if block
    # Assigning and evaluating in if condition only with walrus

    if count := fresh_fruits.get("lemon", 0):
        make_lemonade(count)
    else:
        out_of_stock()
    # Above is better readable

    # Notice parantheses below
    if (count := fresh_fruits.get("lemon", 0)) > 4:
        make_cider(count)
    else:
        out_of_stock()

    # Another eaxmple
    def pick_fruits():
        ...

    def make_juice():
        ...

    bottles = []
    while fresh_fruits := pick_fruits():
        for fruit, count in fresh_fruits.items():
            batch = make_juice(fruit, count)
            bottles.extend(batch)
