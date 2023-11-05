# Nhập giá trị a và b từ người dùng
a = int(input("Nhap gia tri a: "))
b = int(input("Nhap gia tri b: "))

min_value = min(a, b)
# tập hợp để lưu các ước số chung của a và b
s = set()
# Lặp lại các giá trị từ 1 đến min_value và kiểm tra xem giá trị này có phải là ước số của cả a và b không
for i in range(1, min_value + 1):
    if a % i == 0 and b % i == 0:
        s.add(i)
print("Uoc so chung", a, "va", b, "la:", s)