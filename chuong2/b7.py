d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if m == 2:
    if (y % 4 == 0 and y % 100 != 0) or y % 400 :
        if d == 29:
            d = 1
            m = 3
        else:
            d += 1
    else:
        if d == 28:
            d = 1
            m = 3
        else:
            d += 1
elif m in [4, 6, 9, 11]:
    if d == 30:
        d = 1
        m += 1
    else:
        d += 1
else:
    if d == 31:
        if m == 12:
            d = 1
            m = 1
            y += 1
        else:
            d = 1
            m += 1
    else:
        d += 1

print(f"Ngày tiếp theo là: {d}/{m}/{y}")