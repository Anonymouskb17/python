import math
x1 = int(input("Toa so a:"))
y1 = int(input("Toa do a:"))
x2 = int(input("Toa do b:"))
y2 = int(input("Toa do b:"))
x3 = int(input("Toa do c:"))
y3 = int(input("Toa do c:"))

def s(x1,y1,x2,y2,x3,y3):
    return 0.5 * abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))

print("Dien tich:",s(x1,y1,x2,y2,x3,y3))