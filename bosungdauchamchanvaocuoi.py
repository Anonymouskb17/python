s = input("Nhap chuoi: ")
count = 0

for i in range(len(s)-1, -1, -1):
	if s[i] == '!':
		count += 1
	else:
		break

for i in range(3-count):
	s += '!'
print("Chuoi sau khi bo sung dau cham than: '{0}'".format(s))
