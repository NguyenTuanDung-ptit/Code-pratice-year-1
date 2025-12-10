English_dictionary = {
    "hello" : "xin chào",
    "banana" : "quả chuối",
}


while True:

    print("""===== TỪ ĐIỂN ANH VIỆT =====
    1 - Tra từ điển
    2 - Thêm từ điển
    3 - Xóa từ điển
    4 - Thoát chương trình""")

    number = input("Lựa chọn chức năng : ")
    if number == '1':
        while True:
            word = input()
            if word == '0':
                break
            if word in English_dictionary:
                print ("Nghĩa tiếng Việt:", English_dictionary[word])
            else:
                print("Không tìm thấy từ này trong từ điển.")
            stop = input("Bạn có muốn tra tiếp không? (y/n): ")
            if stop != "y":
                break

    elif number == '2':
        while True:
            new_key = input()
            if word == '0':
                break
            if new_key in English_dictionary:
                print("Từ này đã có trong từ điển!")
            else:
                new_value = input("Nhập nghĩa tiếng Việt của từ này: ")
                English_dictionary[new_key] = new_value 
                print("Đã thêm thành công!")
            stop = input("Bạn có muốn thêm tiếp không? (y/n): ")
            if stop != "y":
                break

    elif number == '3':
        while True:
            delete_key = input()
            if delete_key == '0':
                break
            if delete_key in English_dictionary:
                del English_dictionary[delete_key]
                print("Đã xoá thành công!")
            else:
                print("Không tìm thấy từ cần xoá.")
            stop = input("Bạn có muốn thêm tiếp không? (y/n): ")
            if stop != "y":
                break
            
    elif number == '4':
        print("Cảm ơn bạn đã sử dụng TỪ ĐIỂN ANH VIỆT! Hẹn gặp lại ")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        break