# Lấy danh sách các số người dùng nhập vào
nums = [float(input("Nhập một số: "))
        for i in range(int(input("Nhập số lượng số: ")))]

# Tính trung bình cộng và in kết quả
if len(nums) > 0:
    avg = sum(nums) / len(nums)
    print("Trung bình cộng của các số là:", avg)
else:
    print("Không có số nào được nhập vào")
