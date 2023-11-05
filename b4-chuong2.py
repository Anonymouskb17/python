
def tong(n):
    
    tong =0 
    for i in range(0,n):
        tong+=n%10
        n=n//10
    return tong
n= int(input("Nhap n:"))
print("Tong cac chu so: ",tong(n))