n = int(input("Nhap n: "))

# Khởi tạo danh sách với hai giá trị đầu tiên của dãy Fibonacci
fibo = [0, 1]

# Tính toán các giá trị fibo cho đến khi giá trị vượt quá n
while fibo[-1] + fibo[-2] < n:
    fibo.append(fibo[-1] + fibo[-2])

# In ra danh sách các giá trị fibonacci
print(fibo)