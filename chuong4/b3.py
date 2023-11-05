#in ra phần họ và tên nếu giả thuyết họ và tên là 1 âm
name = str(input("Nhap ho ten nguoi la: "))
name_parts = name.split()
ho = name_parts[0]
tendem = name_parts[1]
ten = name_parts[2]
print("Phan ho la:", ho)
print("Phan ten dem la:", tendem)
print("Phan ten la: ",ten)


# # in họ riêng và in ra phần còn lại trong tên
# name = str(input("Nhap ho ten nguoi la: "))
# name_parts = name.split(maxsplit=1)
# ho = name_parts[0]
# ten = name_parts[1]
# print("Phan ho la:", ho)
# print("Phan ten la:", ten)