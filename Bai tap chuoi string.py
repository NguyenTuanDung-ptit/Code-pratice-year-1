# Bài 1
string = input("Bài 1: Nhập một chuỗi vào đây: ")
capitalize_string = string.capitalize()
title_string = string.title()
upper_string = string.upper()
lower_string = string.lower()
print("In hoa chữ cái đầu tiên:", string.capitalize())  #in hoa chữ cái đầu tiên
print("In hoa chữ cái đầu mỗi từ:", string.title())       #in hoa chữ cái đầu mỗi từ
print("In hoa toàn bộ:", string.upper())       #in hoa toàn bộ
print("In thường toàn bộ ", string.lower())       #in thường toàn bộ

# Bài 2
first_name = "Thomas"
last_name = "Edison"
full_name = first_name + " " + last_name     #tên đầy đủ của tác giả
print("Bài 2:", full_name.title() + ":" , "Thiên tài là một phần trăm cảm hứng và chín mươi chín phần trăm mồ hôi.")      #in tên tác giả + trích dẫn câu nói

# Bài 3
text = input("Bài 3: Nhập vào một chuỗi kí tự: ")
print("Chỉ chứa số (0-9):", text.isnumeric())   #chỉ chứa số (0-9)
print("Chỉ chứa kí tự alphabet:" ,text.isalpha())     #chỉ chứa kí tự alphabet
print("Chỉ chứa số và kí tự alphabet:", text.isalnum())     #chỉ chứa số và kí tự alphabet
print("Tất cả kí tự đều viết hoa:" ,text.isupper())     #tất cả kí tự đều viết hoa
print("Tất cả kí tự đều viết thường:" ,text.islower())     #tất cả kí tự đều viết thường

# Bài 4
string_4 = input("Bài 4: Nhập vào một chuỗi gồm nhiều từ cách nhau bởi dấu whitespaces: ")
print("chuỗi vừa nhập có kết thúc bằng từ 'end'" ,string_4.endswith("end"))            #Kiểm tra chuỗi vừa nhập có kết thúc bằng từ "end" hay không
b = string_4.count("is")
if b == 0:
    print("Không có từ 'is'")              #Kiểm tra xem chuỗi có từ "is" hay không
else:
    print("Vị trí xuất hiện đầu tiên của từ 'is':" ,string_4.find("is"))             #In ra vị trí xuất hiện đầu tiên của từ "is"
    print("Số lần xuất hiện từ 'is' trong chuỗi:" ,string_4.count("is"))            #Đếm số lần xuất hiện từ "is" trong chuỗi
print("Thay từ 'is' trong chuỗi thành từ 'are'" ,string_4.replace("is", "are"))       #Thay thế từ "is" bằng từ "are" trong chuỗi
c = string_4.split(" ")
print("Danh sách chứa các từ:" ,c)                                   #Chuyển chuỗi trên thành danh sách chứa các từ
count = 0
for i in c:
    count += 1
    print("Số lượng từ hiện có:" ,count)                           #Đếm số lượng từ hiện có

# Bài 5
S1 = input("Bài 5: Nhập chuỗi kí tự S1: ")
S2 = input("Nhập chuỗi kí tự S2: ")
middle = len(S1) // 2
S = S1[:middle] + S2 + S1[middle:]
print("In ra chuỗi kí tự S được tạo thành bằng cách chèn S2 vào chính giữa S1:" ,S)                                   #In ra chuỗi kí tự S được tạo thành bằng cách chèn S2 vào chính giữa S1

# Bài 6
sum = 0
string_6 = input("Bài 6: Nhập một chuỗi vào đây: ")
digits = string_6.isalpha()
if digits == True:
    print("Come on. I'm so tired!")
else:
    for a in string_6:
        if a in '0123456789':
            sum += int(a)
    print("Tổng các chữ số xuất hiện trong chuỗi:", sum)

# Bài 7
Ex7_S1 = input("Bài 7: Nhập chuỗi S1 vào đây: ")
Ex7_S = input("Nhập chuỗi S vào đây: ")
Ex7_S_cuoi = Ex7_S.replace(Ex7_S1, "")
print("In ra chuỗi S đã xóa S1:" ,Ex7_S_cuoi)

# Bài 8
string_8_1 = input("Bài 8: Nhập 1 chuỗi S1 vào đây: ")
string_8 = input("Nhập 1 chuỗi S vào đây: ")
last_string_8 = string_8.replace(string_8_1, "", 1)
print("Xóa đi S1 lần đầu tiên xuất hiện trong S:" ,last_string_8)

# Bài 9:
string_9 = input("Bài 9: Nhập một chuỗi vào đây: ")
words = string_9.split()
last_9 = words[0]
for i in words:
    if len(i)>= len(last_9):
        last_9 = i
print("Từ dài nhất trong chuỗi là:", last_9)

# Bài 10:
string_10 = input("Bài 10: Nhập một chuỗi vào đây: ")
last_10 = string_10[::-1]
print("Chuỗi đảo ngược S1 là:", last_10)

# Bài 11:
string_11 = input("Bài 11: Nhập một chuỗi vào đây: ")
string_11 = string_11.lower().capitalize()
string_11 =  " ".join(string_11.split())
if string_11.endswith(".") == False:
    string_11 += "."
print("In ra chuỗi đã chuẩn hóa:" ,string_11)