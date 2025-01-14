s = input("Nhap chuoi:")
n = int(input("Nhap so:"))

list = []
for i in s:
    while n>0 and list and list[-1] < i:
        list.pop()
        n-=1
    list.append(i)
while n>0 and list:
    list.pop()
    n-=1

print("Chuoi sau khi xoa:", ''.join(list))