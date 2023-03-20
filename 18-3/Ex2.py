#Viết hàm in ra chuỗi dài nhất mà người dùng nhập

def chuoidainhat(nhapchuoi1, nhapchuoi2):
    if len(nhapchuoi1) > len(nhapchuoi2):
        print("Chuỗi dài nhất",nhapchuoi1)
    else:
        print("Chuỗi dài nhất",nhapchuoi2)

str1 = input("Nhập chuỗi đầu tiên: ")
str2 = input("Nhập chuỗi thứ hai: ")
chuoidainhat(str1,str2)
    

   