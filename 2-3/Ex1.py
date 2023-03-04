#Vòng lặp for 

# month = int(input("Nhập vào một tháng: "))

# for i in range(1, 13):
#     if i == month:
#         if 3 <= i <= 5:
#             print("Tháng", month, "là mùa xuân")
#         elif 6 <= i <= 8:
#             print("Tháng", month, "là mùa hạ")
#         elif 9 <= i <= 11:
#             print("Tháng", month, "là mùa thu")
#         else:
#             print("Tháng", month, "là mùa đông")
#         break
#Vòng lặp while
month = int(input("Nhập vào một tháng: "))

i = 1
while i <= 12:
    if i == month:
        if 3 <= i <= 5:
            print("Tháng", month, "là mùa xuân")
        elif 6 <= i <= 8:
            print("Tháng", month, "là mùa hạ")
        elif 9 <= i <= 11:
            print("Tháng", month, "là mùa thu")
        else:
            print("Tháng", month, "là mùa đông")
        break
    i += 1
