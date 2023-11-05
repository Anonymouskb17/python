n = int(input("Nhap N: "))
a = []
b = []
for i in range(n):
    print('Nhap gia tri thu ', i+1,': ',sep = "",end='')
    x = input()
    try:
        a.append(int(x))
    except:
        try:
            a.append(float(x))
        except:
            b.append(x)
if a!=[]:
    print("Tong cac phan tu cua A =",float(sum(a)))
else:
    print("Tong cac phan tu cua A = 0")
c = sorted(b)
f = c[::-1]
print('B =',f)