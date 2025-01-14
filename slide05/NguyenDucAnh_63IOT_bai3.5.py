n = int(input("N = "))

for i in range(1, n + 1):
    sum = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            sum += j
    if sum > i:
        print(i)
