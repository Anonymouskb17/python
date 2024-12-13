X = int(input("Nhập số nguyên X: "))

# Đếm số chữ số của X
num_digits = len(str(abs(X)))

# Tìm chữ số đầu tiên của X
first_digit = int(str(abs(X))[0])

# In ra số chữ số và chữ số đầu tiên của X
print("Số chữ số của X:", num_digits)
print("Chữ số đầu tiên của X:", first_digit)