'''N= int(input("N = "))
#total_sum = 0
mau= 0
for i in range(1, N+1):
    mau+=N/(sum([j**2 for j in range(1, i+1)]))
    #phanso=N/mau
    #total_sum+=mau
print("F({}) = {:.7f}".format(N,mau))'''


N = int(input("N = "))
def can(k):
    return k * (k+1) * (2*k+1) // 6

tong = 0
for i in range(1, N+1):
        a = can(i)
        b = N / a
        tong += b
print("F({}) = {:.7f}".format(N,tong))




