import math



a= int(input("Nhap canh a: "))
b= int(input("Nhap canh b: "))
c= int(input("Nhap canh c: "))
p= a+b+c
def s(a,b,c):
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Dien tich tam giac ", s(a,b,c))