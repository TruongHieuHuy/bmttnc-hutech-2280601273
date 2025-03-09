# Nhập các dòng từ người dùng
print ("Nhập các dòng từ người dùng(Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)
# Chuyển các dòng thành chữ in hoa và in ra
print ("\nChuyển các dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print (line.upper())