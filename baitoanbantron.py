# n = int(input("So nguoi ngoi quanh ban: "))
# # for i in range(n):
# # 	list1.append(i+1)
# list1 = [i for i in range(1, n+1)]
# count = 0

# i = -1
# while(True):
# 	if len(list1) == 1:
# 		break
# 	if i == len(list1) - 1:
# 		i = -1
# 	count += 1
# 	i += 1
# 	if count == 3:
# 		list1.pop(i)
# 		i -= 1
# 		count = 0
# print(f"Nguoi o lai cuoi cung la nguoi thu {list1[0]}")	

# tong = 1
# s = 0
# n = int(input('N = '))
# for i in range(1, n+1)
# 	tong *= i
# 	if i % 2 == 1:
# 		s += tong
# 	else:
# 		s -= tong
# print(s)


n= int(input("So nguoi ngoi quanh ban: "))
def find(n):
    last =0
    for i in range(2,n+1):
        last= (last+3)%i
    return last
last = find(n)
print("Nguoi o lai cuoi cung la nguoi thu", last+1)