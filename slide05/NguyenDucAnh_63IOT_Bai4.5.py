import re
n= input("Nhap email:")
s = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', n)
if s:
    print("Email hop le")
else:
    print("Email khong hop le")
