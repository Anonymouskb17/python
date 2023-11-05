
S = input("Nhap chuoi: ")
kiemtra = True
for i in range(len(S)//2):
    if S[i] != S[i-1]:
        kiemtra = False
        break
if kiemtra:
    print("Chuoi S la doi xung")
else:
    print("Chuoi S khong phai dang doi xung")
    
#bài chưa đúng, xem lại