import calendar


def get_days_in_month():
    while True:
        try:
            month = int(input("Nhập vào một tháng (1-12): "))
            if month < 1 or month > 12:
                raise ValueError
            break
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")

    year = calendar.monthrange(2023, month)[0]
    days_in_month = calendar.monthrange(2023, month)[1]
    return days_in_month


# Gọi hàm và in ra số ngày trong tháng
days_in_month = get_days_in_month()
print(f"Số ngày trong tháng: {days_in_month}")
