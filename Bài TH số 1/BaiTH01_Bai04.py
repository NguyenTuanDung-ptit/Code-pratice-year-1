math = float(input("Nhập điểm Toán: "))
language = float(input("Nhập điểm Văn: "))
english = float(input("Nhập điểm Anh: "))
average = (math + language + english) / 3
result = round(average, 2)
print("Điểm trung bình:", result)