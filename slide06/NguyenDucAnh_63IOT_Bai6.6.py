
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
def uocsochung(a, b):
    uocsotapA = {d for d in range(1, a + 1) if a % d == 0}
    uocsotapB = {d for d in range(1, b + 1) if b % d == 0}
    return uocsotapA & uocsotapB

result = uocsochung(a, b)
print("Các ước số chung của a và b là:", result)
