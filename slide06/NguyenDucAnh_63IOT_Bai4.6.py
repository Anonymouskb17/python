# sinhvien = []

# while True:
#     full_name = input("Nhập họ và tên sinh viên: ")
#     if full_name == "":
#         break
#     sinhvien.append(full_name)
# print("Danh sách sinh viên:")
# for student in sinhvien:
#     name_parts = student.split()
#     ten = name_parts[0]
#     ho = " ".join(name_parts[1:])
#     print(f"Họ: {ten}, Tên: {ho}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
name = []
while True:
    fullname = input("Nhap ho va ten:")
    if fullname == "":
        break
    name.append(fullname)
for names in name:
    name_spart= names.split()
    ten = name_spart[0]
    ho = "".join(name_spart[1:])
    print(f"Ho: {ten}, Ten: {ho}")
