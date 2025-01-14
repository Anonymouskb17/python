n = int(input("N = "))
a = [1]
for i in range(n*10):
	a.append(2*a[i] + 1)
	a.append(3*a[i] + 1)

b = set(a) # Dung set(tap hop)

a.clear()
a = list(b)
a.sort() # Tham so dao nguoc (reverse = false)>>default

print(n, "so dau tien cua N23:", end=" ")
for i in range(n):
	if i < n-1:
		print(a[i], end=" ")
	else:
		print(a[i])