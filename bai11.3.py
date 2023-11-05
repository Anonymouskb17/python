def NT(N):
    # Phân tích N thành các thừa số nguyên tố
    factors = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            factors.append(i)
            N //= i
        else:
            i += 1
    if N > 1:
        factors.append(N)
    return factors
N = int(input("Nhap n: "))
factors = NT(N)
print("Cac thua so NT ", N, "la:", factors)