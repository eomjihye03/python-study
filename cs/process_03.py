import os
from multiprocessing import Process

def foo():
    print("Hello, os")

if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()