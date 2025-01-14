list =[]
n = int(input("Nhập số n:"))
for i in range(n+1):
    if i%2!=0:
        list.append(i)
print("Số lẻ từ 1 đến 199 là:",list)