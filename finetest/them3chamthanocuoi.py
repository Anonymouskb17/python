# s = str(input("Nhap chuoi: "))
# if '!'  not in s:
#         print(f"Chuoi sau khi bo xung dau cham than: '{s}!!!'")
# else:
#     print(f"Chuoi sau khi bo xung dau cham than: '{s}!!'")
#     if '!!'  in s:
#         print(f"Chuoi sau khi bo xung dau cham than: '{s}!!'")
#     elif '!!!' in s:
#         print(f"Chuoi sau khi bo xung dau cham than: '{s}'")

# Nhập chuỗi S từ bàn phím
S = input("Nhap S: ")

# Kiểm tra và thêm dấu chấm than nếu cần
if not S.endswith('!!!'):
    S += '!!!'

# In ra chuỗi S sau khi được xử lý
print("Chuoi S sau khi xu ly:",S)
