list = []
while True:
    num = input("Nhập số nguyên và bấm x để dừng: ")
    if num == 'x':
        break
    data = int(num)
    list.append(data)

set = set(list)
print(set)