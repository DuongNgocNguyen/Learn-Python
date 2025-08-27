# Ép kiểu từ kiểu dữ liệu nhỏ -> lớn hơn
# Ví dụ: int -> float -> complex (a + bj)
a = "1.5+2.5j"  # Remove spaces
b = complex(a)

print(f"Value of b: {b}")
print(f"Type of b: {type(b)}")