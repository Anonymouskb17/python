import math
x1= int(input())
y1= int(input())
x2= int(input())
y2= int(input())
x3= int(input())
y3= int(input())
print("Toa do A:" ,x1,y1)
print("Toa do B:" ,x2,y2)
print("Toa do A:" ,x3,y3)

def area2(x1,x2,x3,y1,y2,y3):
    return 0.5*abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))
print(area2(x1,x2,x3,y1,y2,y3))