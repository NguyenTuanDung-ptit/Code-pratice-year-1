import string

punctuation_list = string.punctuation
text = input()
list = []
strip_text = text.strip()

for i in strip_text:
    if i != " " and i not in punctuation_list:
        list.append(i)

list_reverse = list[::-1]
if list == list_reverse:
    print("true")
if list != list_reverse:
    print("false")