S = str(input("Nhap chuoi: "))
N = int(input("Nhap so nguyen: "))

list = []
for c in S:
    while N > 0 and list and list[-1] < c:
        list.pop()
        N -= 1
    list.append(c)

while N > 0 and list:
    list.pop()
    N -= 1

result = ''.join(list)
print("Chuoi moi la:", result)