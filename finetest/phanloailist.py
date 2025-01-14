
# N = int(input("Nhap N: "))
# A = []
# B = []
# C = []
# for i in range(N):
#     x = input("Nhap gia tri thu %d: " %(i+1))
#     try:
#         x = int(x)
#         A.append(x)
#     except ValueError:
#         try:
#             x = float(x)
#             B.append(x)
#         except ValueError:
#             C.append(x)
# A.sort(reverse=True)
# B.sort(reverse=True)
# C.sort(reverse=True)
# print("A =",A)
# print("B =",B)
# print("C =",C)

N = int(input("Nhap N: "))
A = []
B = []
C = []
for i in range(1,N+1):
    x = input("Nhap gia tri thu "+str(i)+": ")
    if x.isdigit() or '-1'<=x<='-9' or x=='0' or x=='-0':
        x=int(x)
        A.append(x)
    elif x.count('.')==1:
        x=float(x)
        B.append(x)
    else:
        C.append(x)
print("A =",(sorted(A,reverse=True)))
print("B =",(sorted(B,reverse=True)))
print("C =",(sorted(C,reverse=True)))       