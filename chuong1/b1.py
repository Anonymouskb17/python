#bài 1.1
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
delta = b*b-4*a*c
if delta==0:
    print("Nghiem kep: x = ", str(-b/2/a))
if delta<0:
    print("Phuong trinh vo nghiem")
if delta>0:
    print("X1 = " + str((-b+delta**0.5)/2/a))
print("X2 = " + str((-b-delta**0.5)/2/a))

#bài 1.2
def giaithua(n):
    gt = 1
    for i in range(2, n+1):
        gt = gt * i
    return gt
a = int(input("Nhập giá trị n: "))
print("N! =", giaithua(a))

#bài 1.3
a = int(input("A = "))
b = int(input("B = "))
while (b > 0):
  if (a > b):
    a, b = b, a % b
else:
    a, b = a, b % a
print("Ước số chung lớn nhất là:", a)