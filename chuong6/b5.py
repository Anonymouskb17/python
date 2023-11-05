# Nhập giá trị N từ người dùng
N = int(input("Nhap N "))

# Khởi tạo tập hợp để lưu các ước số của N
uocso = set()

# Lặp lại các giá trị từ 1 đến N và kiểm tra xem giá trị này có phải là ước số của N không
for i in range(1, N + 1):
    if N % i == 0:
        uocso.add(i)

# In ra tập hợp các ước số của N
print("Uoc so cua ", N, "la:", uocso)

