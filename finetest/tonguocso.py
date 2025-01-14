import math
n = int(input("N = "))
sum = 0
#N= int(math.sqrt(n))
for i in range(1,n+1):
        if n % i == 0:
            sum += i
print("Tong cac uoc so cua {} la {}".format(n,sum))

'''n= int(input("N = "))
def sum_of_divisors(n):
    u = int(math.sqrt(n)) 
    total_sum = 0
    for i in range(1, u+1):
        if u % i == 0:
            total_sum += i
    return total_sum

divisor_sum = sum_of_divisors(n)
print("Tong cac uoc so cua {} la {}".format(n, divisor_sum))'''



'''import math
N = int(input("N = "))
total_sum = 0
sqrt_N = int(math.sqrt(N))
for i in range(2, sqrt_N+1):
        if N % i == 0:
            total_sum += i
            if i != N // i:
                total_sum += N // i
print("Tổng các ước số của {} là {}".format(N, total_sum))

def sum_of_divisors(n):
    sum_divisors = 1
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            sum_divisors *= ((i**(count+1)) - 1)//(i - 1)
        i += 1
    if n > 1:
        sum_divisors *= (n + 1)
    return sum_divisors
'''




