
N = int(input("Nhập số nguyên dương N: "))

mu = 2 ** N
#chuyển giá trị thành chuỗi
num = str(mu)

# Khởi tạo biến tổng sum_digits
sum = 0

# Lặp qua từng chữ số trong chuỗi
for digit in num:
    # Chuyển chữ số thành số nguyên và cộng vào tổng
    sum += int(digit)

# In ra tổng các chữ số
print("Tổng các chữ số của số 2^N:", sum)