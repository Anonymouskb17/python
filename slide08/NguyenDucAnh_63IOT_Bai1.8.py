try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    if b == 0:
        raise ZeroDivisionError("b không thể bằng 0.")
    print(f"Kết quả của {a}/{b} là: {a / b}")
except ValueError:
    print("Vui lòng nhập một số nguyên.")
except ZeroDivisionError as e:
    print(e)
