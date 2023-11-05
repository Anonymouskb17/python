# Lấy chuỗi đầu vào và tách thành các số riêng lẻ
S = input("Nhap so: ")
numbers = S.split()

# Chuyển đổi các số sang kiểu số nguyên và tạo tập hợp
s = set(map(int, numbers))

# In ra số phần tử, giá trị lớn nhất và giá trị nhỏ nhất của tập hợp
print("So phan tu trong tap hop la:", len(s))
print("Gia tri lon nhat trong tap hop la:", max(s))
print("Gia tri nho nhat trong tap hop la:", min(s))