s = "dai hoc thuy loi"
dic = {}
for char in s:
    dic[char] = dic.get(char, 0) + 1
print("Từ điển số lần xuất hiện:", dic)
