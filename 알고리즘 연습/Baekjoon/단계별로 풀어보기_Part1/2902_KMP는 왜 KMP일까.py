S = input()

string = ''
for i in S:
    if i.isupper() == True:
        string += i
print(string)