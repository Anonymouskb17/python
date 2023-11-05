S = input("Nhập dãy số nguyên:")

# Chuyển đổi dãy số thành danh sách các số nguyên
S = [int(num) for num in S.split(',')]
# Tạo danh sách rỗng để lưu trữ số chẵn và số lẻ
sochan = []
sole = []
# Lặp qua từng số trong dãy và đưa số chẵn vào sochan và số lẻ vào sole
for num in S:
    if num % 2 == 0:
        sochan.append(num)
    else:
        sole.append(num)
# Sắp xếp sochan theo thứ tự giảm dần và sole theo thứ tự tăng dần
sochan.sort(reverse=True)
sole.sort()
# Kết hợp sochan và sole để tạo dãy số đã sắp xếp
sorted_sequence = sochan + sole

# In ra dãy số đã sắp xếp
print("Dãy số đã sắp xếp:", sorted_sequence)