#Vòng for
width = int(input("Nhap chieu rong: "))
height = int(input("Nhap chieu dai: "))

for i in range(height):
    print('*' * width)

#Vòng while
width = int(input("Nhap chieu rong: "))
height = int(input("Nhap chieu dai: "))

i = 0
while i < height:
    j = 0
    while j < width:
        print('*', end='')
        j += 1
    print()
    i += 1
