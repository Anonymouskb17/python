S = input("Nhập chuỗi S: ")

# Khởi tạo tập hợp rỗng để lưu trữ các chuỗi con khác nhau
sub1 = set()

# Lặp qua từng vị trí i trong chuỗi S
for i in range(len(S)):
    # Lặp qua từng vị trí j từ i đến độ dài S
    for j in range(i, len(S)):
        # Trích xuất chuỗi con từ vị trí i đến vị trí j+1 trong chuỗi S
        sub2 = S[i:j+1]
        # Thêm chuỗi con vào tập hợp
        sub1.add(sub2)

# In ra màn hình tất cả các chuỗi con khác nhau
for sub2 in sub1:
    print(sub2)