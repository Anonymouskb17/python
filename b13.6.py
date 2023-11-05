def last_person(N):
    # Khởi tạo danh sách các người ngồi quanh bàn tròn
    people = list(range(1, N + 1))

    # Vị trí bắt đầu đếm
    index = 0

    # Lặp cho đến khi chỉ còn lại 1 người
    while len(people) > 1:
        # Tính vị trí của người bị loại khỏi bàn
        index = (index + 2) % len(people)
        
        # Loại bỏ người khỏi danh sách
        people.pop(index)

    # Trả về người cuối cùng ngồi lại
    return people[0]

# Nhập số người ngồi quanh bàn N từ người dùng
N = int(input("Nhập số người ngồi quanh bàn: "))

# Tính người cuối cùng ngồi lại
last_person = last_person(N)

# In kết quả
print("Người cuối cùng ngồi lại là:", last_person)