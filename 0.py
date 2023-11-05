s = input("Nhap S: ")
dem,n = 0,len(s)
for i in range(n):
    if s[i] == '!':
        dem += 1
if dem % 2 == 1:
    s = s + str('!')
elif dem == 0:
    s = s + str('!!')
print("Chuoi S sau khi xu ly:",s)