print("NHAP BANG GIA:")
A = dict()
maxLen = int(0)
while (1):
    sp = input("  Ten mat hang: ")
    if (sp == ""):
        break
    maxLen = max(len(sp), maxLen)
    gia = float(input("  Gia ban hang: "))
    w = {sp : gia}
    A.update(w)

B = dict()
print("NHAP HANG TON:")
Max = float(0)
while(1):
    sp = input("  Ten mat hang: ")
    if (sp == ""):
        break
    ton = int(input("  So luong ton kho: "))
    Max = max(Max, ton * A.get(sp))
    w = {sp : ton * A.get(sp)}
    B.update(w)

for i in A:
    if i not in B:
        w = {i : float(0)}
        B.update(w)

#Ls = B.items()
#Ls.sort(key=lambda x:x[1], reverse=True)

C = sorted(B.items(), reverse=False, key = lambda x : (Max - x[1], x[0]))
#print(C)

print("THONG KE HANG TON:")
for i in C:
    value = str(format(i[1],".2f"))
    print(" ", i[0].ljust(maxLen), value.rjust(6))
