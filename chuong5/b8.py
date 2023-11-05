#đang sai, cần xem lại
N = input()
def generate_strings(X, N):
#đệ quy để trả về giá trị trong tupple x nhỏ hơn n
    if N == 0:
        return ['']
    else:
        strings = []
        for s in X:
            for t in generate_strings(X, N-len(s)):
                strings.append(s + t)
        return strings
X = ('()',)
# Liệt kê tất cả các chuỗi có độ dài ít hơn 4 của tuple X
strings = generate_strings(X, N)
print(strings)

