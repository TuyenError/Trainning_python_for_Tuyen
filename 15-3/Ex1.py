# Tạo hàm tìm số lớn nhất giữa 3 số

def Timso(a,b,c,d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= c and b >= a and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    else:
        return d

x = int (input("nhap"))
y = int (input("nhap"))
z = int(input("nhap"))
h = int(input("nhap"))

print(Timso(x, y, z,h))

    