danh_sach = []
while True:
    input_value = input("Nhập danh sách số và bấm x để dừng: ")
    if input_value == 'x':
        break
    number = int(input_value)
    danh_sach.append(number)
new_list = [x for x in danh_sach if int(x) < 10]
print("Danh sách mới chứa các số < 10:", new_list)