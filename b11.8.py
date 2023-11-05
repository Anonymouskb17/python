S = input("Nhập chuỗi S: ")

# Khởi tạo tập hợp rỗng để lưu trữ các chuỗi con khác nhau
str1 = set()

# Lặp qua từng vị trí i trong chuỗi S
for i in range(len(S)):
    # Lặp qua từng vị trí j từ i đến độ dài S
    for j in range(i, len(S)):
        # chuỗi con từ vị trí i đến vị trí j+1 trong chuỗi S
        sub = S[i:j+1]
        # Kiểm tra xem chuỗi con đã trích xuất có trong tập hợp chưa
        if sub not in str1:
            # Nếu chưa có, thêm chuỗi con vào tập hợp
            str1.add(sub)
            # In ra chuỗi con
            print(sub)