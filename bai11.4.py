def doixung(n):
    num1= str(n)
    num2= num1[::-1]
    return num1== num2

def sdx(n):
    # Tìm số đối xứng lớn nhất nhỏ hơn N
    for num in range(n-1, 0, -1):
        if doixung(num):
            return num
    return -1
n= int(input("Nhap n:"))
a= sdx(n)
print("so doi xung",a)