def tao_dict():
    danh_sach = {}

    for i in range(3):
        print(f"Người thứ {i + 1}:")
        ten = input("Nhập tên: ")
        tuoi = int(input("Nhập tuổi: "))
        danh_sach[ten] = tuoi

    print(danh_sach)

tao_dict()