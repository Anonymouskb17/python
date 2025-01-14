def nhaptudien(prompt):

    nhap = input(prompt)
    tudien = {}
    for item in nhap.split(","):
        key, value = item.split(":")
        tudien[key.strip()] = int(value.strip())
    return tudien

a = nhaptudien("Nhập từ điển A: ")
b = nhaptudien("Nhập từ điển B: ")

c = {}
for key in set(a) | set(b):
    if key in a and key in b:
        c[key] = max(a[key], b[key])
    elif key in a:
        c[key] = a[key]
    else:
        c[key] = b[key]

print("Từ điển C:", c)
