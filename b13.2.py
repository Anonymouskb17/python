def sobenhat(A, B):
    A = list(map(int, A.split()))
    B = set(map(int, B.split()))
#hàm map dùng để thực hiện 1 funtion đối với 1 chuỗi dữ liệu
    min_number = float('inf')

    for num in A:
        if num not in B and num < min_number:
            min_number = num
    
    if min_number == float('inf'):
        print("Khong co")
    else:
        print("So nho nhat la:", min_number)


# Nhập dãy A và B từ người dùng
A = input("Nhập dãy A: ")
B = input("Nhập dãy B: ")

# Tìm số nhỏ nhất trong A mà không có trong B
sobenhat(A, B)