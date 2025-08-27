""" 
Viết chương trình nhập vào 2 số nguyên và in ra:
	- Tổng
	- Hiệu
	- Tích
	- Thương (làm tròn 2 chữ số thập phân)
"""

a = int(input("Nhap so thu nhat:"))
b = int(input("Nhap so thu hai:"))

tong = a + b
hieu = a - b
tich = a * b
#thuong = round(a / b, 2)

print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print("Thương: %.2f"%(float(a)/b))# f-strings