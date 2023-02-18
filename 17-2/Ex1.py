#Bài 1 : Nhập tháng bất kỳ, trả lời tháng đó có bao nhiêu ngày?
# Dùng vòng lặp while

n = int(input("Nhập tháng: "))
day=0

while n < 0 or n >  12 :
    n = int(input("Tháng không hợp lệ. Nhập lại tháng: "))
if n == 2:
    year = int(input("Nhập năm: "))

    while year < 1:
        year = int(input("Năm không hợp lệ. Nhập lại năm  "))
    if year % 4 == 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
elif n == [4,6,9,11]:
    day = 31
else:
    day = 30
print(f"Tháng {n} có {day} ngày.")











