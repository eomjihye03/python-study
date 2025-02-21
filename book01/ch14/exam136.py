# 상속 (inheritance)

class Vehicle:
    def __init__(self, model, maker, capacity=2):
        self.model = model
        self.maker = maker
        self.capacity = capacity
    def __str__(self):
        return f'모델: {self.model}\n제조사: {self.maker}\n탑승인원: {self.capacity}명\n'
    
class Battery:
    def __init__(self, ah):
        self.ah = 100
    def __str__(self):
        return f'배터리: {self.ah}Ah'

class Car(Vehicle):
    def __init__(self, model, maker, cc, capacity=2,):
        super().__init__(model, maker, capacity)
        self.cc = cc
    def __str__(self):
        return super().__str__() +\
            f'\n총배기량: {self.cc}cc'

class Truck(Car):
    def __init__(self, model, maker, cc, weight, capacity=2):
        super().__init__(model, maker, cc, capacity)
        self.weight = weight
    def __str__(self):
        return super().__str__() + f'\n중량: {self.weight}톤'
v = Vehicle('차량', '현대')
c = Car('소나타', '현대', 1980, 4)
t = Truck('타이탄', '현대', 10000, 10)

print(v)
print(c)
print(t)

# 다중 상속
class ElecCar(Vehicle, Battery):
    def __init__(self, model, maker, ah, capacity=2):
        super().__init__(model, maker, capacity) # Vehicle 생성자 호출
        Battery.__init__(self, ah) # 두 번째 부모 Battery는 생성자를 직접 호출.
    def __str__(self):
        return super().__str__() + f'{Battery.__str__(self)}'

ec = ElecCar('아이오닉9', '현대', 110, 5)
print(ec)