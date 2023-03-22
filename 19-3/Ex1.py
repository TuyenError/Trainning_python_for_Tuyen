def  TuDien(ma, mb , nhap):
    a = 0
    for i in range(1,len(mb)+1):
        if mb[i-1] == nhap:
            a=i
    if a > 0:
        for i in range(1,len(ma)+1):
            return ma [a-1]
    else:
        return "Không có"


Keys = ['Ten', 'Twenty', 'Thirty']
Values = [10, 20, 30]
Nhap = int(input("Nhâp: "))
print(TuDien(Keys,Values,Nhap))