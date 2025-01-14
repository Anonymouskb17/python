n= float(input("Nhập số điểm:"))


if 0<=n<3.5:
    print("Xếp loại yếu")
elif 3.5<=n<5:
    print("Xếp loại kém")
elif 5<=n<6.5:
    print("Xếp loại trung bình")
elif 6.5<=n<8:
    print("Xếp loại khá")
elif 8<=n<9:
    print("Xếp loại giỏi")
else:
    print("Xếp loại xuất sắc")