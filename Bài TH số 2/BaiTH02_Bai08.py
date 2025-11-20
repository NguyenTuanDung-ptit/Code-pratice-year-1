danh_sach = []
while True:
    input_value = input("Nhập số và bấm x để dừng: ")
    if input_value in 'x':
        break
    number = int(input_value)
    danh_sach.append(number)
print("Tổng các số trong dãy:", sum(danh_sach))
print("Trung bình các ố trong dãy:", sum(danh_sach) / len(danh_sach))
print("Số lớn nhất:", max(danh_sach))