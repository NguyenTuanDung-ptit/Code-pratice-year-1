danh_sach = []
sum = 0
while True:
    input_value = input("Nhập danh sách số và bấm x để dừng: ")
    if input_value == 'x':
        break
    number = int(input_value)
    danh_sach.append(number)
for value in danh_sach:
    if value % 2 == 0:
       sum += value
print("Tổng các số chẵn:", sum)