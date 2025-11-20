score = float(input("Nhập điểm trung bình: "))
if score > 10 or score < 0:
    print("Điểm không hợp lệ")
elif score < 5:
    print("Yếu")
elif score >= 5 and score <= 6.4:
    print("Trung bình")
elif score >= 6.5 and score <= 7.9:
    print("Khá")
else:
    print("Giỏi")