'''
s = 'DHTHUYLOI'
print(len(s))
print(s[3:7])
print('THU' in s)
print(s[::-1])

print('ket qua bieu thuc la:%f' % (2.5*30))
print('ten truong la: %s' %('dhthuyloi'))
print('a:{},  b:{}, c:{}'.format(1,2,3))


print('a: {1}, b: {2}, c: {0}'.format('one', 'two', 'three')) 
print('two same values: {0}, {0}'.format(1, 2)) 
'''
#bai1
'''
i= str(input(''))
if ( '!!!' not in i):
    print(i+'!!!')
else:
    print("Nhap lai")
'''
#bai2
'''i = str(input("nhap: "))
while i =='0':
     if(i!=0):
         print(i)
     else:
         print(i)'''

#bai3
'''h = str(input(''))
ho=h.split()
print("Ho :",ho[0])
print("Ten:",ho[2])'''


#bài4
'''s=str(input("Nhap chuoi:"))
a=s.replace('1','a'[5])
print(a)'''



#bai1
'''a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
if a+b<c & b+c<a % a+c<b:
    print("Khong phai tam giac")
else:
    print("Dung la tam giac")'''


#bài2
'''s = str(input("Nhap S:"))
if ( '!' in s):
    a =s.replace('!','')
    print(a)
else:
    print("Chuoi s sau khi lại bo dau cham than",s)'''

#bai3
'''import math
n = int(input("N = "))
s= 0
for i in range(1,n+1):
    s=s+math.sqrt((1+i)*i/2)
print("F({}) = {:.7f}".format(n,s))'''




l1 = list()

n = [[x,x+x] for x in range(100)]
print(n)
