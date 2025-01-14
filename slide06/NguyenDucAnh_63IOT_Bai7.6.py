n = input("Nhập dãy số nguyên: ")
s = n.split(";")

result = set(s)
print(f"Số lượng các số khác nhau trong dãy là: {len(result)}")
