import math
tien = 10000000
print("Số tiền sau 10 năm:", int(tien * (1 + 0.51)**10))
dich = 5e7 
nam = math.log(dich / tien, 1 + 0.51) 
print("Số năm để có ít nhất 50 triệu:", math.ceil(nam))