string, word = map(str, input("").split())
for i in string:
    if i != word:
        print(i, end = '')