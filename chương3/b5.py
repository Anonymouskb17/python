import math
numbers = []
while True:
    num = int(input("Nhap so tu nhien la: "))
    if num <= 0:
        break
    numbers.append(num)
print("Day nhap la:", numbers)
print("Uoc chung lon nhat la:",math.lcm(*numbers))
print("Boi chung nho nhat la:",math.gcd(*numbers))