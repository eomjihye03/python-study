import os
from multiprocessing import Process

def foo():
    print("I am foo!!")
def bar():
    print("I am bar!!")
def baz():
    print("I am baz!!")

if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()