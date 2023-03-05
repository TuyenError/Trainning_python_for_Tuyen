#for
n=4
for i in range (1,n+1):
    for j in range(i):
        print("*" , end='')
    print("")

#while
n = 4
i = 0
while i < n:
    j =1
    while j <= i:
        print("*", end='')
        j+=1
    print()
    i+=1