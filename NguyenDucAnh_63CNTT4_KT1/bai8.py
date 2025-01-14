words = input("Nhập dãy các từ, cách nhau bằng dấu cách: ").split()
longest_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == longest_length]
print("Từ dài nhất:", longest_words)