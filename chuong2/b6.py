a=int(input())
b=int(input())
c=int(input())
'''f a>b>c and a>c>b:
    print(a)
elif a<b<c and c>a>b:
    print(c)
elif b>c>a and b>a>c:
    print(b)'''
if a >= b and a >= c:
    print(a)
   
elif b >= a and b >= c:
    print(b)
  
else:
    print(c)
  