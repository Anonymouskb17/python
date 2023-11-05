import math
x = int(input("Nhập số nguyên X ="))
len = math.floor(math.log10(x))
print("Số chữ số của X:", len + 1)
print("Chữ số đầu tiên của X:", x // 10**len)
