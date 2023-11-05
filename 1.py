n = int(input("N = "))
SUM = 0
for i in range (2,n+1,2):
   SUM = SUM + i**2
print("P(",n,") = ", SUM ,sep = "")
