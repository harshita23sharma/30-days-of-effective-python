"""
Prefer Catch-all unpacking.
"""


def generate_csv():
    yield ("Date", "Make", "Model", "Year", "Price")
    ...


def run():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_desc = sorted(car_ages, reverse=True)
    oldest, *others, recent = car_ages_desc
    print(oldest, recent, others)  # 20 0 [19, 15, 9, 8, 7, 6, 4, 1]

    # Star expressions become list instances in all cases

    # Better to use star exp instead of indexing and slicing
    # With indexing and slicing
    all_csv_rows = list(generate_csv())
    header = all_csv_rows[0]
    rows = all_csv_rows[1:]
    print(
        "CSV Header:", header
    )  # CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
    print("Row count", len(rows))  # Row count 0

    # Using starred expression

    it = generate_csv()
    header, *rows = it
    print(
        "CSV Header:", header
    )  # CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
    print("Row count", len(rows))  # Row count 0

    # Unpacking the iterator using *, also risks in using up all memory
    # So only use this catch-all unpacking on iterators when you have good
    # reason to believe that the result data will all fit in memory


if __name__ == "__main__":
    run()
