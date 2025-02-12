# 리스트로 큐 구현

from collections import deque 

myqueue = deque([])

def offer(value):
    myqueue.append(value)

def poll():
    if len(myqueue) == 0:
        return None
    return myqueue.popleft()

offer("Damon")
offer("Elena")
offer("Matt")

print(myqueue)


while value := poll(): # Boolean context
    print(value)

