s = str(input("Nhap chuoi:"))

for i in s:
    if not i.isalpha():
         s=s.replace(i, '?')
print(s)
