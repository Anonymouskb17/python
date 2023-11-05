n =int(input("Nhap n:"))

def  total(n):
    sum=0
    for i in range(0,n):
        sum +=n%10
        n=n//10
    return sum
print("Tong la:",total(n))
    