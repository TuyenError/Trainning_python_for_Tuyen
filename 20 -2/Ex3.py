#Vòng for
r = int(input("Nhap chieu rong: "))
d = int(input("Nhap chieu dai: "))

for i in range(d):
    for j in range(r):
        print('*', end='')
    print()

#Vòng while
r = int(input("Nhap chieu rong: "))
d = int(input("Nhap chieu dai: "))

i = 0
while i < d:
    j =0
    while j < r:
        print ('*',end='')
        j = j+1
    print()
    i=i+1


