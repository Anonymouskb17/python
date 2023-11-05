def calculate_angle(time):
    # Chuyển đổi thời gian thành giờ và phút
    hours, minutes = map(int, time.split(':'))

    # Tính góc của kim giờ
    hour_angle = (hours + minutes/60) * 30

    # Tính góc của kim phút
    minute_angle = minutes * 6

    # Tính góc giữa hai kim
    angle = abs(hour_angle - minute_angle)

    return round(angle, 2)

# Nhập chuỗi thời gian T từ người dùng
time = input("Nhập thời điểm T (hh:mm): ")

# Tính góc giữa hai kim giờ và phút
angle = calculate_angle(time)

# In kết quả
print("Góc giữa hai kim là:", angle, "độ")