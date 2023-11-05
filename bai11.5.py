
num = input("Nhap day so =: ").split(",")
num = [int(num) for num in num]

tongday = sum(num)

# Tính bình phương của tổng
squared_sum = tongday ** 2
sum_of_squares = sum([num ** 2 for num in num])
difference = squared_sum - sum_of_squares
print("Chenh lech la: ", difference)