s = input("Nhap day so: ")
# Tách các số ra thành một danh sách
numbers = s.split(";")
# Tạo ra một tập hợp các số duy nhất từ danh sách numbers
num = set(numbers)
count = len(num)
print("Day so nhap vao", count, "so khac nhau")