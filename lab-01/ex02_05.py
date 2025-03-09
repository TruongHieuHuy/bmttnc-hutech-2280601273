# Nhập giờ làm và lương
gio_lam = int(input("Nhập số giờ làm: "))
luong_gio = int(input("Nhập lương: "))
# Số giờ làm chuẩn mỗi tuần
gio_lam_chuan = 54
# Số giờ làm vượt chuẩn
gio_vuot_chuan = max (0, gio_lam - gio_lam_chuan)
# Tổng thu nhập
tong_thu_nhap = gio_lam * luong_gio + gio_vuot_chuan * luong_gio * 1.5
# In ra
print(f"Tổng thu nhập:", {tong_thu_nhap})