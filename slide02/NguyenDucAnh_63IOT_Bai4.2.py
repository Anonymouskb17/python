


def tong(n):
    #n = int(input("Nhap so nguyen:"))
    total = 0
    while n > 0:
        total += n % 10
        n= int(n/10)
    return total
        
print("Tong cac chu so cua so nguyen la:", tong(132))