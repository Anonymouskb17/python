a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a%2 == 0 and b%2 == 0 and c%2 == 0:
	print("Cung tinh chan le")
elif a%2 == 1 and b%2 == 1 and c%2 == 1:
	print("Cung tinh chan le")
elif a==b==c:
	print("Cung tinh chan le")
else:
	print("Khac tinh chan le")