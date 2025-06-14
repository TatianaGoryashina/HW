import math


def square():
    side = int(input("Введите сторону квадрата: "))
    if isinstance(side, int):
        result = side * side
    else:
        result = math.ceil(side * side)
    print(f"Площадь квадрата: {result}")


square()
