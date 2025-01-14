
def UCLN(a,b):
    while b:
        a,b= b, a%b
    return a
def BCNN(a,b):
    return a*b//UCLN(a,b)

def list():
    n =[]
    while True:
        a = int(input("Nhap: "))
        if (a<0):
            break
        n.append(a)
        #n+= str(a)
    
    numberUC = n[0]
    numberBC = n[0]
    for i in n:
        numberUC = UCLN(numberUC,i)
        numberBC = BCNN(numberBC,i)
    print("UCLN: ",numberUC)
    print("BCNN: ",numberBC)
list()







        
        
    
    

