words = input("Nhap day: ")
listword = words.split()
longword = ""
max_length = 0

for word in listword:
    if len(word) > max_length:
        longword = word
        max_length = len(word)

longwords = [word for word in listword if len(word) == max_length]

print("Tu dai nhat:", longword)
print("Tat ca cac tu co do dai nhat la:", longwords)