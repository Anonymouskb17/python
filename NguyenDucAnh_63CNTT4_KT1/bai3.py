n= int(input("Nhap n:"))
def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n
    else:
        return False
    
 


