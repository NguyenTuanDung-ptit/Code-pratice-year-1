while True: 
    num = float(input("Nhập số điện: "))
    if num >= 0 and num <= 50:
        print("Tiền điện:", num * 1800, "đ/kWh")
        break
    elif num >= 51 and num <= 100:
        print("Tiền điện:", 50 * 1800 + (num - 50) * 2000, "đ/kWh")
        break
    elif num > 100:
        print("Tiền điện:", 50 * 1800 + 50 * 2000 + (num - 100) * 2500, "đ/kWh")
        break
    else:
        print("Số điện không hợp lệ. Vui lòng nhập lại.")
        