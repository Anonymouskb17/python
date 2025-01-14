n = int(input("Nhap so nguyen n:"))

count=0
num = str(n)
for i in num:
    if(i.isdigit()):
        count+=1
    
print("So chu so la:", count)
print("Chu so dau tien la:",num[0])
    