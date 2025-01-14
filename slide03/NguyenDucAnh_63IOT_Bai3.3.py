a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))

def UCLN(a,b):
    while b:
        a,b= b, a%b
    return a

def BCNN(a,b):
    return a*b//UCLN(a,b)    
                
print("UCLN cua",a,"va",b,"la",UCLN(a,b))
print("BCNN cua",a,"va",b,"la",BCNN(a,b))