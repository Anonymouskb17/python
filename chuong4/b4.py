s = str(input("Nhap chuoi: "))
new_s = ""

for char in s:
    if not char.isdigit():
        new_s += char

print("Chuoi moi la:", new_s)