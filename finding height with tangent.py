import math
while True:
    length = float(input("enter the length: "))
    deg = float(input("enter the deg: "))
    deg = math.tan(deg * math.pi / 180)
    print(deg * length)
