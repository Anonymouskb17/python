N = int(input("Nhập một số nguyên N: "))
def result(N):
    uocso = {d for d in range(1, N + 1) if N % d == 0}
    return uocso

print("Các ước số của N:", result(N))