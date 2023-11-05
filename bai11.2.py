def fibo(n):
    a,b=0,1
    while b<=n:
        a,b=b,a+b
    return a

n= int(input("Nhap n:"))
a= fibo(n)
print(a)
