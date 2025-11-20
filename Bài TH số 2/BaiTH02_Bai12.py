danh_sach = []
while True:
    input_value = input("Nhập danh sách số và bấm x để dừng: ")
    if input_value == 'x':
        break
    number = int(input_value)
    danh_sach.append(number)
max_appear = danh_sach[0]
appear = 0
for value in set(danh_sach):
    now_appear = danh_sach.count(value)
    if now_appear > appear:
        appear = now_appear
        max_appear = value

print(f"Phần tử {max_appear} xuất hiện nhiều nhất với {appear} lần")