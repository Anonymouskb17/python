# Khởi tạo danh sách để lưu trữ thông tin về họ và tên của sinh viên
s = []

# Lặp lại việc nhập liệu cho đến khi người dùng gõ vào một dòng trống
while True:
    st = str(input("Nhap ho ten sinh vien "))
    if st == "":
        break
    s.append(st)

# In ra danh sách họ và tên của sinh viên
print("Ho ten sinh vien la:")
for student in s:
    print(student)
    
    
