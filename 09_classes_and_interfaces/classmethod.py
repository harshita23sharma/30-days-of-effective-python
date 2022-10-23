"""
Use @classmethod to define alternative constructor (apart from __init__) for your classes
Use class method polymorphism to provide generic way to build & connect many concrete subclasses
"""
import os
# Implementing mapreduce in a generic way to construct objects.
# Each InputData suclass provides a special constructor that can be
# used generically by the helper methods that orchestrate the MapReduce
# SImilar to factory pattern 

class GenericInputData:
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    ...

    @classmethod
    def generate_inputs(clas, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    def map(self):
        raise NotImplementedError
    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
            return workers

class LineCountWorker(GenericWorker):
    ...

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

config = {"data_dir": "tmpdir"}
result = mapreduce(LineCountWorker, PathInputData, config)
print(f"There are {result} lines")