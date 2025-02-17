# 상속 (inheritance)

class Vehicle:
    def __init__(self, model, maker, capacity=2):
        self.model = model
        self.maker = maker
        self.capacity = capacity
    def __str__(self):
        print(f'모델: {self.model}')
        print(f'제조사: {self.maker}')
        print(f'탑승인원: {self.capacity}')

class Car(Vehicle):
    def __init__(self, model, maker, cc, capacity=2,):
        super().__init__(model, maker, capacity)
        self.cc = cc
    def __str__(self):
        super().__str__()
        print(f'배기량: {self.cc}')

class Truck(Car):
    def __init__(self, model, maker, cc, weight, capacity=2):
        super().__init__(model, maker, cc, capacity)
        self.weight = weight


v = Vehicle('차량', '현대')
c = Car('소나타', '현대', 1980, 4)
t = Truck('타이탄', '현대', 10000, 10)

print(v)
print(c)
print(t)