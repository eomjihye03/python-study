import threading
import os

def foo():
    print("I'm foo!!!")
    print("thread id", threading.get_native_id())
    print("process id", os.getpid())
    print("*" * 50)
    
def bar():
    print("I'm bar!!!")
    print("thread id", threading.get_native_id())
    print("process id", os.getpid())
    print("*" * 50)

def baz():
    print("I'm baz!!!")
    print("thread id", threading.get_native_id())
    print("process id", os.getpid())
    print("*" * 50)

if __name__ == '__main__':
    print("process id", os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()

# 세 개의 스레드 모두 각기 다른 스레드지만, 이들은 모두 동일한 프로세스를 공유하고 있다.