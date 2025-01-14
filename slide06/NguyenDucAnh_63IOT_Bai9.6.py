
Pnhansu = set(map(int, input("Nhập mã nhân viên phòng nhân sự: ").split(',')))
Phanhchinh = set(map(int, input("Nhập mã nhân viên phòng hành chính: ").split(',')))
Ptruyenthong = set(map(int, input("Nhập mã nhân viên phòng truyền thông: ").split(',')))

tongnhanvien = Pnhansu | Phanhchinh | Ptruyenthong
print(f"Tổng số nhân viên sử dụng trong công ty: {len(tongnhanvien)}")


manv = Pnhansu & Phanhchinh & Ptruyenthong
print(f"Các mã nhân viên thuộc cả 3 phòng: {manv}")


phong = (Pnhansu - Phanhchinh - Ptruyenthong) | \
                (Phanhchinh - Pnhansu - Ptruyenthong) | \
                (Ptruyenthong - Pnhansu - Phanhchinh)
print(f"Các mã nhân viên chỉ thuộc 1 phòng: {phong}")

from itertools import combinations

phongs = {
    "Pnhansu-Phanhchinh": len(Pnhansu & Phanhchinh),
    "Pnhansu-Ptruyenthong": len(Pnhansu & Ptruyenthong),
    "Phanhchinh-Ptruyenthong": len(Phanhchinh & Ptruyenthong),
}
chungphong = max(phongs.values())
chungphongnhieunhat = [room for room, count in phongs.items() if count == chungphong]
print(f"Cặp phòng dùng chung nhiều nhân viên nhất ({chungphong} nhân viên): {chungphongnhieunhat}")

print(f"Mã nhân viên đầu tiên của phòng nhân sự: {min(Pnhansu)}")
print(f"Mã nhân viên đầu tiên của phòng hành chính: {min(Phanhchinh)}")
print(f"Mã nhân viên đầu tiên của phòng truyền thông: {min(Ptruyenthong)}")
