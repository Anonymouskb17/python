try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Cạnh tam giác phải là số dương.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Không tạo thành tam giác được.")

    print("Đây là một tam giác.")
except ValueError as e:
    print(e)
except Exception:
    print("Giá trị không hợp lệ.")
