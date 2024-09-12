from math import sqrt

# Đọc file "TRAI.txt"
with open("TRAI.txt") as f:
    a = f.read()  # Đọc toàn bộ nội dung file
a = a.split()  # Tách các phần tử theo khoảng trắng

# Lấy độ dài của danh sách các số trong file
_len = len(a)
tr = 0  # Biến đếm các trại

# Vòng lặp tính toán khoảng cách
for i in range(0, _len, 2):
    # Tính khoảng cách giữa 2 tọa độ (x, y) bằng định lý Pythagoras
    d = sqrt(int(a[i])**2 + int(a[i+1])**2)
    _d = round(d, 2)  # Làm tròn kết quả khoảng cách đến 2 chữ số thập phân
    tr += 1  # Tăng số lượng trại đã tính
    # In ra khoảng cách tới trại
    print(f"Khoảng cách đến các trại {tr} là: {_d}")