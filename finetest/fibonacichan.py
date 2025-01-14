def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n
n = int(input("N = "))
if is_fibonacci(n) and is_fibonacci(n-1) and n % 2 == 0:
    print("N la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")