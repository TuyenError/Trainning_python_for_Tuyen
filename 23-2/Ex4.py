#Vòng lặp for 
for i in range(1, 11):
    row = ""
    for j in range(1, 11):
        row += str(i*j) + " "
    print(row)


#While
i = 1
while i <= 10:
    j = 1
    row = ""
    while j <= 10:
        row += str(i*j) + "\t"
        j += 1
    print(row)
    i += 1
