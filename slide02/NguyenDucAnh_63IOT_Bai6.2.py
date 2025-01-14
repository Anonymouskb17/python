a = int(input("Nhập số thứ nhất:"))
b = int(input("Nhập số thứ hai:"))
c = int(input("Nhập số thứ ba:"))

if (a>b>c ):
    print("Số lớn nhất là:", a)
elif b>a>c :
    print("Số lớn nhất là:", b)
elif c>a>b:
    print("Số lớn nhất là:", c)
elif b==c>a:
    print("Số còn lại là:", a)  
elif a==c>b:
    print("Số còn lại là:",b)      
elif a==b>c:
    print("Số còn lại là:",c)
