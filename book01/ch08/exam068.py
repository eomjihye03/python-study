# 리스트로 스택 구현

mystack = []

def pushData(value):
    mystack.append(value)

def popData():
    if len(mystack) == 0:
        return None
    return mystack.pop()

pushData("Damon")
pushData("Elena")
pushData("Matt")

print(mystack)


while value := popData(): # Boolean context
    print(value)
