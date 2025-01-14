N = int(input("Nhập số lượng người chơi: "))
songuoichoi = []
for i in range(N):
    nguoichoi = set(map(int, input(f"Nhập số thứ {i + 1}: ").split()))
    songuoichoi.append(nguoichoi)

songuoithang = set(map(int, input("Nhập 6 số của giải đặc biệt: ").split()))

nguoithang = []
for i, nguoichoi in enumerate(songuoichoi):
    if len(nguoichoi & songuoithang) >= 5:
        nguoithang.append((i + 1, nguoichoi))

if nguoithang:
    print("Những người thắng cuộc:")
    for idx, nguoichoi in nguoithang:
        print(f"Người chơi {idx} với số {nguoichoi}")
else:
    print("Không có người chơi nào thắng.")
