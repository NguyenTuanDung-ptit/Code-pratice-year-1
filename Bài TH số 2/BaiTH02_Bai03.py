string = input("Nhập một chuỗi tiếng Anh: ")
nguyen_am = 0
phu_am = 0
for i in string:
    if i in 'aeiouAEIOU':
        nguyen_am += 1
    else:
        phu_am += 1
print("Số lượng nguyên âm:", nguyen_am)
print("Số lượng phụ âm:", phu_am)