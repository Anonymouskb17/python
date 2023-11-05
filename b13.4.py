def pin(N, H):
    dem = N

    for hour in range(1, H ):
        if hour % 2 == 0:
            dem *= 2
        else:
            dem += int(dem * 0.3)
    
    return dem

# Nhập số vi khuẩn ban đầu N và số giờ H từ người dùng
N = int(input("Nhập số vi khuẩn: "))
H = int(input("Nhập số giờ: "))

# Tính số vi khuẩn sau H giờ
result = pin(N, H)

# In kết quả
print("Số vi khuẩn sau", H, "giờ là:", result)