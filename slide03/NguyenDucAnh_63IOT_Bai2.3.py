a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))

def isPrime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print("Cac so nguyen to trong day (",a,",",b,") la: ", end="")
for i in range(a,b+1):
    if isPrime(i):
        print(i, end=" ")

