'''list=input("Nhap chuoi: ")
l1= list.split()
a= [int(list) for i in l1]
print(a)
n= int(input("Nhap chuoi:"))
list=[]
for i in range(n):
    value= ("So thu {}".format(i+1))
    list.append(value)
print("Chuoi nhap la:",list)'''


'''n= int(input("Nhap N:"))
a=[]
b=[]
for i in range(n):
    value= input("Nhap gia tri thu {}".format(i+1))
    try:
        if '.' in value:
            a.append= int(value)
    except ValueError:
            b.append= float(value)
if len(a)>0:
    c= sum(a)/ len(a)
    print("Trung binh cong cua day so la:",c)
print(b)'''

'''def add_value(value, A, B):
    try:
        num = int(value)
        A.append(num)
    except ValueError:
        try:
            num = int(value)
            A.append(num)
        except ValueError:
            B.append(value)
N = int(input("Nhập số nguyên dương N: "))
A = []
B = []
for i in range(N):
    value = input("Nhập giá trị thứ {}: ".format(i+1))
    add_value(value, A, B)
if len(A) > 0:
    avg_A = sum(A) / len(A)
    print("Trung bình cộng các phần tử của danh sách A là:", avg_A)
print("Danh sách B:", B)'''


N = int(input("Nhap N: "))
A = []
B = []
for i in range(N):
    value = input("Nhap gia tri thu {}: ".format(i+1))
    if '.' in value:
        try:
            A.append(float(value))
        except ValueError:
            B.append(value)
    else:
        try:
            A.append(int(value))
        except ValueError:
            B.append(value)
if len(A) > 0:
    avg_A = sum(A) / len(A)
    print("TBC cua A =",avg_A)
print("B =",B)