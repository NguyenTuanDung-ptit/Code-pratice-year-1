n = int(input("Nhập một số 1-9: "))
print("Bảng cửu chương của", n)
for i in range (1,11):
    a = i * n
    print(n, "x", i, "=", a)