numbers = []
while True:
    num = int(input("Nhập một số tự nhiên: "))
    if num < 0:
        break
    numbers.append(num)
print("Dãy số bạn vừa nhập là:", numbers)