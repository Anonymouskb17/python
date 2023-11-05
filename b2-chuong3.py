
def snt(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a= int(input("Nhap a:"))
b= int(input("Nhap b:"))   
 
for n in range(a,b+1):
    if snt(n):
        print(n) 
        
