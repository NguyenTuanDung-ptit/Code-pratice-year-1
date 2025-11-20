
danh_sach = []
while True:
    input_value = input("Nhập danh sách và nhấn x để dừng: ")
    if input_value.lower() in 'x':
        break
    danh_sach.append(input_value)
last_string = danh_sach[::-1]
print(last_string)