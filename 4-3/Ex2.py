def print_n_lines(n, string):
    for i in range(n):
        print(string)


# Gọi hàm và in ra n dòng của chuỗi
n = int(input("Nhập số nguyên n: "))
string = input("Nhập chuỗi str: ")
print_n_lines(n, string)
