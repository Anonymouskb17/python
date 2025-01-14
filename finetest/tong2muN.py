# n = int(input("N = "))

# # Tính giá trị của 2N
# num = pow(2,n)

# # Tính tổng các chữ số của giá trị num
# tong = 0
# while num > 0:
#     tong += num % 10
#     num //= 10


# print("Tong =",tong)


n = int(input("N = "))
s = 0

if n>=0:
 for i in str(2**n):
  s += int(i)
 print("Tong =", s)