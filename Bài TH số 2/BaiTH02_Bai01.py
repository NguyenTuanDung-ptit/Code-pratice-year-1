string = input("Nhập vào một chuỗi: ")
print("Độ dài chuỗi:", len(string))
from collections import Counter
dem_so = Counter(string)
print(f"Số lần xuất hiện của mỗi kí tự {dem_so}")