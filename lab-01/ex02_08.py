# Kiẻm tra số nhị phân chia hết cho 5
def chia_het_cho_5(so_nhi_phan):
# Chuyển số nhị phân sang thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    return False
# Nhập chuỗi số nhị phân
chuoi_so_nhi_phan = input("Nhập số nhị phân (phân tách bởi dấu phẩy): ")
# Tách chuỗi thành các số nhị phân và kiểm tra số chia hết cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
# In kết quả
if len(so_chia_het_cho_5) > 0:
    print(f"Các số nhị phân sau chia hết cho 5: {', '.join(so_chia_het_cho_5)}")
else:
    print("Không có số nào chia hết cho 5") 
