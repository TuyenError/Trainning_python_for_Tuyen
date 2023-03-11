def input_month():
    while True:
        try:
            month = int(input("Nhập vào tháng (1-12): "))
            if month < 1 or month > 12:
                raise ValueError
            else:
                return month
        except ValueError:
            print("Tháng không hợp lệ. Vui lòng nhập lại.")


def find_season(month):
    if month in (1, 2, 12):
        return "Mùa Đông"
    elif month in (3, 4, 5):
        return "Mùa Xuân"
    elif month in (6, 7, 8):
        return "Mùa Hạ"
    else:
        return "Mùa Thu"


# gọi hàm để nhập tháng và tìm mùa
month = input_month()
season = find_season(month)
print(f"Tháng {month} nằm trong mùa {season}.")
