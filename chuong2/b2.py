import math
a= int(input())
b= int(input())
c= int(input())
p=a+b+c
def area(a,b,c):
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
print(area(a,b,c))