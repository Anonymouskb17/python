# n = input("Nhap n:")
# d = {n}
# for i in d:
#     if i ==0 or i==1:
#         break
#     else:
#         print(max())

D = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
sorted_values = sorted(D.values(), reverse=True)

for value in sorted_values[:3]:
    print(value)
