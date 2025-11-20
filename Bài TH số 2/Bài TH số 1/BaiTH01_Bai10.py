year = int(input("Nhập một năm: "))
if year % 400 == 0:
    print("Năm nhuận")
elif year % 4 == 0 and year % 100 != 0:
    print("Năm nhuận")
else:
    print("Năm không nhuận")