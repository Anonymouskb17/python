def tangdan(sub):
    sub1 = []  # Danh sách các dãy con
    sub0 = []  # Dãy con hiện tại

    for i in range(len(sub)):
        if i == 0 or sub[i] > sub[i-1]:
            sub0.append(sub[i])
        else:
            sub1.append(sub0)
            sub0 = [sub[i]]

    sub1.append(sub0)  # Thêm dãy con cuối cùng

    return sub1

# Nhập dãy số nguyên từ người dùng
sub = input("Nhập dãy số nguyên: ")

# Chuyển đổi dãy số thành danh sách các số nguyên
sub = [int(num) for num in sub.split(',')]

# Tách dãy thành các dãy tăng dần
sub1 =tangdan(sub)

# In ra các dãy con
for sub_sub in sub1:
    print(sub_sub)