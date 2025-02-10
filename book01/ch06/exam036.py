# 클래스로 Iterator 만들기

class MyIterator:
    def __init__(self, obj):
        self.obj = obj
        self.cursor = 0

    def __next__(self):
        if self.cursor < self.obj.max:
            value = self.cursor
            self.cursor += 1
            return value
        else:
            raise StopIteration

class MyRange:
    def __init__(self, n):
        self.max = n
    
    def __iter__(self):
        return MyIterator(self)
    

my_range = MyRange(5)
my_iterator = my_range.__iter__()
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())


my_range = MyRange(5)
my_iterator = iter(my_range)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))