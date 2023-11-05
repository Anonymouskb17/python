def khonglapk(string, k):
    n = len(string)
    
    # Tạo một tập hợp để lưu trữ các chuỗi con độ dài k
    sub1 = set()
    
    for i in range(n - k + 1):
        sub_string = string[i:i+k]
        if sub_string in sub1:
            return False
        sub1.add(sub_string)
    
    return True
string = input("Nhập chuỗi nhị phân: ")
k = int(input("Nhập giá trị k: "))
# Kiểm tra xem chuỗi có là không lặp bậc-k hay không
if khonglapk(string, k):
    print("Chuỗi là không lặp bậc-k.")
else:
    print("Chuỗi không là không lặp bậc-k.")