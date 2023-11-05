# import math
# n = int(input("N = "))
# s= 0
# for i in range(1,n+1):
    
#     s+=math.pow(i+1,)
    
# print("F ({}) = {:.7f}".format(n,s))


# '''import math
# n= int(input("N = "))
# tong = 0
# #F=0
# for i in range(1,n+1):
#     tong+=i
#     a=math.pow(tong,1/n)
#     F = tong/a
    
# print(f"F({n}) = {F:.7F}")'''


import math
n= int(input("N = "))
tong= 0
f=0
for i in range(1,n+1):
    tong += i
    f += tong**(1/i)
print("F(",n,") = %0.7f"%f,sep='')





'''import math
n= int(input("N = "))
def tong(n):
    t=0
    for i in range(1,n+1):
        t+= math.sqrt(i)
        return tong
print(f"F({n}) = {tong}")'''


'''from math import sqrt
N = int(input("Nhập số nguyên dương N: "))
tong_can_bac_hai = 0
tong = 0
for i in range(1, N+1):
    tong += i
    tong_can_bac_hai += sqrt(tong)
F = 1 + tong_can_bac_hai / N
print(f"Giá trị của hàm F({N}) là: {F:.7f}")'''
