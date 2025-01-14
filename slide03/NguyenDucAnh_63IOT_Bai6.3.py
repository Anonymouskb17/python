n= int(input("Nhap n: "))
k= int(input("Nhap k: "))

def fibo(n,k):
    if n<k:
        return k
    else:
        sum=0
        for i in range(1,k+1):
            sum+=fibo(n-i,k)
        return sum

print("Ket qua la: ",fibo(n,k))
            
