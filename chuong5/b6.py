import math

# Khởi tạo mảng bool với tất cả các giá trị ban đầu đều là True
values = [True] * 1000000

# Đánh dấu các bội số của các số nguyên tố là False
for i in range(2, int(math.sqrt(1000000))+1):
    if values[i]:
        for j in range(i**2, 1000000, i):
            values[j] = False

# Tạo tuple P chứa các số nguyên tố
P = tuple(i for i in range(2, 1000000) if values[i])
print(P)