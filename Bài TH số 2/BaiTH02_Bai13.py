danh_sach_1 = []
while True:
    input_value_1 = input("Nhập danh sách số 1 và bấm x để dừng: ")
    if input_value_1 == 'x':
        break
    number_1 = int(input_value_1)
    danh_sach_1.append(number_1)

danh_sach_2 = []
while True:
    input_value_2 = input("Nhập danh sách số 2 và bấm x để dừng: ")
    if input_value_2 == 'x':
        break
    number_2 = int(input_value_2)
    danh_sach_2.append(number_2)
new_list = danh_sach_1 + danh_sach_2
print(new_list)
print("Danh sách mới đã sắp xếp:", sorted(new_list))