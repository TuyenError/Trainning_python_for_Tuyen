str = "Cao Tuyen"
i = 0
while i < len(str):
    if str[i] != ' ':  #! = " " Kiểm tra khoản trắng
        print(str[i])
    i += 1

str = "Cao Tuyen"
for char in str: #Ký tự trong chuỗi
    if char != ' ':
        print(char)
