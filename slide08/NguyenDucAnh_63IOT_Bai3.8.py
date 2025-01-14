def ktra(num):
    return num % 2 == 0

def bai3():
    numbers = []

    while True:
        try:
            n = input("Nhập số nguyên dương: ")
            if not n.isdigit() and not (n[0] == '-' and n[1:].isdigit()):
                raise ValueError("Lỗi nhập số")
            num = int(n)
            if num == 0:
                print("Kết thúc chương trình.")
                break
            if num < 0:
                raise ValueError("Lỗi số âm!!!")
            numbers.append(num)
            if len(numbers) >= 4 and len(set(numbers[-4:])) == 1:
                raise ValueError("Lỗi nhập lặp")
            if len(numbers) >= 5 and all(ktra(n) for n in numbers[-5:]):
                raise ValueError("Lỗi nhập chẵn")
        except ValueError as e:
            print(e)
            continue
bai3()
