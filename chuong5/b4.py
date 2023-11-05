import re

email = input("Nhap dia chi: ")
diachi = r"[^@]+@[^@]+\.[^@]+"
if re.match(diachi, email):
    print("Dia chi email hop le")
else:
    print("Dia chi email khong hop le")