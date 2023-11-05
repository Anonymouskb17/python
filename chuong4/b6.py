words = input("Nhap tu: ")
dem = {}

for word in words.split():
    for letter in word:
        if letter.isalpha():
            if letter in dem:
                dem[letter] += 1
            else:
                dem[letter] = 1

print("So lan xuat hien chu cai la:")
for letter, count in dem.items():
    print(f"{letter}: {count}")