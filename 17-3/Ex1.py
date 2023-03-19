#Tìm số lớn nhất và nhỏ nhất trong mảng
array = [2,1,4,5,-5,-8]
max = 0
a = 0
min = 0
for i in array:
    if (i >= (array[a+1])):
        max = i

for i in array:
    if (i <= (array[a-1])):
        min = i

print(max)
print(min)
