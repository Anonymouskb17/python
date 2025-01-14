d = int(input("Nhap ngay:"))
m = int(input("Nhap thang:"))
y = int(input("Nhap nam:"))

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 :
        if d==31:
            print("Ngay moi 1/",m+1,"/",y)
        elif 1<=d<31:
            print("Ngay moi ",d+1,"/",m,"/",y)
elif m==4 or m==6 or m==9 or m==11:
        if d==30:
            print("Ngay moi 1/",m+1,"/",y)
        elif 1<=d<30:
            print("Ngay moi ",d+1,"/",m,"/",y)
elif m==12:
    if d==31:
        print("Ngay moi 1/1/",y+1)
if y%4==0 and y%100!=0 or y%400==0:
    if m==2:
        if d==29:
            print("Ngay moi 1/",m+1,"/",y)
        elif 1<=d<29:
            print("Ngay moi ",d+1,"/",m,"/",y)
else:
    if m==2:
        if d==28:
            print("Ngay moi 1/",m+1,"/",y)
        elif 1<=d<28:
            print("Ngay moi ",d+1,"/",m,"/",y)

                
                

    