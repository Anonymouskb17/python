a= float(input("Nhap so a:"))
b= float(input("Nhap so b:"))
c= float(input("Nhap so c:"))

if a>b>c or a==b>c or a==c>b or b==c<a:
    print(a)
elif b>a>c or a==b>c or b==c>a or a==c<b :
    print(b)
elif c>b>a or c==b>c or a==c>b or a==b<c:
    print(c)
