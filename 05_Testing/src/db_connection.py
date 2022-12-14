import time


class DBConnector:
    def __init__(self):
        # setup some db connection
        time.sleep(3)
        pass

    def get(self, id):
        time.sleep(5)
        return "some data"


class Engine:
    def __init__(self):
        # How can we test Engine.load_data? When mock __init__ function,
        # we must put return_value with None.
        self.connector = DBConnector()

    def load_data(self):
        data = self.connector.get(123)
        print(data)
        # do some processing
        data = data + "xxx"
        return data
