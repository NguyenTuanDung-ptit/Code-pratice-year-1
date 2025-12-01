def reverse(danh_sach):
    n = len(danh_sach)

    for i in range(n // 2):
        j = n - 1 - i
        danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
    
    return danh_sach

list = [10, 20, 30, 40, 50]
print(f"Ban đầu:   {list}")

ket_qua = reverse(list)
print(f"Đảo ngược: {ket_qua}")