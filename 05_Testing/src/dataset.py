import time


def load_data():
    time.sleep(4)
    # loading data...
    return {"key1": "val1", "key2": "val2"}


def process_data():
    data = load_data()
    # process the data in certain ways ...
    processed_data = data["key1"]
    return processed_data
