data = []
count = 0
while True:
    num = input("Nhập số nguyên và bấm x để dừng: ")
    if num == 'x':
        break
    int_num = int(num)
    data.append(int_num)
for i in data:
    if i % 2 == 0:
        count += 1

print("Có", count, "số chẵn.")