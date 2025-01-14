import random

luongmua = {month: [random.uniform(100, 4000) for _ in range(20)] for month in range(1, 13)}
print("Lượng mưa trung bình mỗi tháng (2002-2021):")
for month, values in luongmua.items():
    print(f"Tháng {month}: {values}")
