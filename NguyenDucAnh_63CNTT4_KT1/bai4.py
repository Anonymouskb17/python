import math
a= int(input("Đỉnh a:"))
b= int(input("Đỉnh b:"))
c= int(input("Đỉnh c"))
p=a+b+c
def area(a,b,c):
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
print(area(a,b,c))