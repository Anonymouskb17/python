C = input("Nhập dãy C: ")
N = int(input("Nhập số nguyên N: "))

min_diff = float('inf')
result = ""

for i in range(len(C) - N + 1):
    subsequence = C[i:i+N]
    max_digit = max(subsequence)
    min_digit = min(subsequence)
    diff = int(max_digit) - int(min_digit)
    if diff < min_diff:
        min_diff = diff
        result = subsequence

print("Dãy con có chênh lệch bé nhất:", result)