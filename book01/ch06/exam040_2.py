# list() - 사용자 정의 클래스

class Car:
    def __init__(self, model, maker, cc):
        self._model = model
        self._maker = maker
        self._cc = cc
        self._cursor = 0
    
    def __str__(self):
        return f'{self._model}, {self._maker}, {self._cc}'

    def __iter__(self):
        return self

    def __next__(self):
        print("__next__() 호출!!!")
        self._cursor += 1
        match (self._cursor):
            case 1:
                return self._model
            case 2:
                return self._maker
            case 3:
                return self._cc
            case _:
                raise StopIteration


    

c1 = Car('소나타', '현대자동차', 1980)
print(c1)

print(list(c1))