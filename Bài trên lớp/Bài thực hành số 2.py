#Bài thực hành số 2

#Bài 1
string = input()
print("Độ dài chuỗi là:", len(string))
word = input()
print("Số lần xuất hiện của", word, "là:", string.count(word))

#Bài 2
string2 = input()
if string2 == string2[::-1]:
    print("Đối xứng")
else:
    print("Không đối xứng")

#Bài 3
string3 = input()
for i in string3:
    if i in 'aeiouAEIOU':
        d = [i]
        print(len(d))
        print(len(string3) - len(d))

#Bài 4
string4 = input()
print(string4.title())

#Bài 5
string5 = input()
print(string5.replace('Python', 'AI'))

#Bài 6
string6 = input()
print(string6.split())
print("-".join(string6))

#Bài 7
cau = input()
print(len(cau.split()))

#Bài 8
day_so = 
                  