from collections import Counter

list = []
while True:
    num = input("Nhập số nguyên và bấm x để dừng: ")
    if num == 'x':
        break
    data = int(num)
    list.append(data)

count = Counter(list)
print(count.most_common(1))