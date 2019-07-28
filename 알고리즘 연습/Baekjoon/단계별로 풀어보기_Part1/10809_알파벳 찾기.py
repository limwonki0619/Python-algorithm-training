s = input()
for i in range(26):
    alphabet = chr(i+ord('a'))
    if alphabet in s:
        print(s.find(alphabet), end=' ')
    else:
        print(-1, end=' ')

