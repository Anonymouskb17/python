import math
n = int(input("N = "))
s= 0
for i in range(1,n+1):
    s+=math.sqrt((1+i)*i/2)
print("F({}) = {:.7f}".format(n,s))

