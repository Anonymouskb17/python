def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

A = int(input("Nhập số A: "))
B = int(input("Nhập số B: "))

print("Các số nguyên tố trong khoảng [{}, {}]: ".format(A, B))
for num in range(A, B + 1):
    if is_prime(num):
        print(num)