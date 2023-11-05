def boiso(N):
    sum = 0
    for i in range(1, N):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

N = int(input("Nhap so nguyen duong N: "))
result = boiso(N)
print("Tong cac so la boi so cua 3 hoac 5 nho hon", N, "la:", result)