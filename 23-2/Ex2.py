str = "Cao Tuyen"
char = 0
for i in str:
    char=char-1
    if i == "T":
        str=str[:char]+str[char+1:]
print(str)