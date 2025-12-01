list_1 = []
print("Nhập set 1")
while True:
    num_1 = input("Nhập số nguyên và bấm x để dừng: ")
    if num_1 == 'x':
        break
    data_1 = int(num_1)
    list_1.append(data_1)

list_2 = []
print("Nhập set 2")
while True:
    num_2 = input("Nhập số nguyên và bấm x để dừng: ")
    if num_2 == 'x':
        break
    data_2 = int(num_2)
    list_2.append(data_2)

set_1 = set(list_1)
set_2 = set(list_2)

set_3 = set_1 & set_2
set_4 = set_1 | set_2
set_5 = set_1 - set_2

print(f"Giao: {set_3}")
print(f"Hợp: {set_4}")
print(f"Hiệu: {set_5}")