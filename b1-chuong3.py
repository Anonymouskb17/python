n =int(input("Nhap n:"))


def snt(n):
    for i in range (2, int(n**0.5)+1):
        if n % i ==0:
            return False
    return True
    
print(n,"la so nguyen to: ",snt(n))
