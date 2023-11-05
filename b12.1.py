S= input("Nhập dãy số nguyên: ")

# Chuyển đổi dãy số thành danh sách các số nguyên
S = [int(num) for num in S.split(',')]

# Tạo dãy từ 1 đến N
N = len(S)
ex = list(range(1, N + 1))

# Kiểm tra xem dãy vừa nhập có phải là dãy hoán vị của dãy từ 1 đến N hay không
if S == ex:
    print("la day hoan vi", N)
else:
    print("khong phai day hoan vi", N)