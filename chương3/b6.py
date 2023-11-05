def fibo(n, k):
    if n < k:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibo(n-1, k) + fibo(n-2, k)
    else:
        result = 0
        for i in range(k):
            result += fibo(n-i-1, k)
        return result
n = int(input("Nhập giá trị của n: "))
k = int(input("Nhập giá trị của k: "))

print("Gía trị của hàm fibo(n, k) là:", fibo(n, k))