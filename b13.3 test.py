def biendoi(N):
    sub1 = [N]
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = 3 * N + 1
        sub1.append(N)
    return sub1

# Nhập số nguyên dương N từ người dùng
N = int(input("Nhập số nguyên dương N: "))

# Tính quá trình biến đổi Collatz cho N
collatz_sub1 = biendoi(N)

# In ra quá trình biến đổi
print("Quá trình biến đổi Collatz cho", N, "là:")
print(" → ".join(str(num) for num in collatz_sub1))