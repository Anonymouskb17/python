# n = int(input("Nhap so nguyen n:"))

# def isPrime():
#     if n<=1:
#         return False
#     elif n==2:
#         return True
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# if isPrime():
#     print(n, "la so nguyen to")
# else:
#     print(n,"khong la so nguyen to")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
n = int(input("Nhap so nguyen n:"))
def isPrime():
    if n<=1:
        return False
    elif n ==2:
        return True
    for i in range(2,n):
        if n %i==0:
            return False
        return True

if isPrime():
    print(n, "la so nguyen to")
else:
    print(n, "khong la so nguyen to")
    