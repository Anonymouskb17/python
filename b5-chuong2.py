n= float(input())
if(n>0 and n<=10):
    if n<3.5:
        print("Loai yeu")
    elif 3.5<=n<5:
        print("Loai kem")
    elif 5<=n<=6.5:
        print("Loai trung binh")
    elif 6.5<=n<8:
        print("Loai kha")
    elif 8<=n<9:
        print("Loai gioi")
    elif 9<=n:
        print("Loai xuat sac")
else:
    print("khong hop le")