def sum_of_proper_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

n = int(input("Nhập số n: "))

for num in range(1, n):
    if sum_of_proper_divisors(num) > num:
        print(num)
