n = int(input("Nhap n:"))
print("Tam giác:")
for i in range(n): 
    for j in range(i+1):
        print("*",end="")
    print()