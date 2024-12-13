S = input("Nhập chuỗi S: ")
N = int(input("Nhập số nguyên N: "))

deleted_count = 0
while deleted_count < N:
    max_digit = max(S)
    S = S.replace(max_digit, '', 1)
    deleted_count += 1

print("Chuỗi sau khi xóa:", S)