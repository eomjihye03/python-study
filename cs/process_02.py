import os
from multiprocessing import Process

def foo():
    print("child process", os.getpid())
    print("my parent process is", os.getppid())

if __name__ == '__main__':
    print('parent process', os.getpid())
    child = Process(target=foo).start()
