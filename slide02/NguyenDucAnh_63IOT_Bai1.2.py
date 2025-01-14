a= int(input("Nhập số thứ nhất:"))
b = int(input("Nhập số thứ hai:"))
c = int(input("Nhập số thứ ba:"))
d = int(input("Nhập số thứ tư:"))
e = int(input("Nhập số thứ năm:"))


def ave():
    return int((a+b+c+d+e)/5)

print("Trung bình cộng của 5 số:", ave())