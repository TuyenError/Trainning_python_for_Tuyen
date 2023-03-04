n =5
for i in range(n):
    for j in range(i+1):
        print(j+1, end='')
    print()

n = 5
i = 0
while i < n:
    j =0
    while j <= i:
        print(j+1, end='')
        j+=1
    print()
    i+=1