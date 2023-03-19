arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr_chan = []
arr_le = []

for num in arr:
    if num % 2 == 0:    # kiểm tra số chẵn
        arr_chan.append(num)    # thêm số chẵn vào mảng arr_chan
    else:
        arr_le.append(num)    # thêm số lẻ vào mảng arr_le

print("Mảng arr_chan chứa các số chẵn là:", arr_chan)
print("Mảng arr_le chứa các số lẻ là:", arr_le)
