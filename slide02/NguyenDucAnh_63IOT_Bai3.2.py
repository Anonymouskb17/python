print(3**2)
import math
print("Nhap toa do canh thu nhat:")
x1 = int(input())
y1 = int(input())
print("Nhap toa do canh thu hai:")
x2 = int(input())
y2 = int(input())
print("Nhap toa do canh thu ba:")
x3 = int(input())
y3= int(input())

def dientich():
    
    return 0.5*abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))

print("Dien tich tam giac la:", dientich())