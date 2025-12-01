def trung_binh_tuple(danh_sach):
    if not danh_sach: return 0, 0

    nhom_x, nhom_y = zip(*danh_sach)
    
    x = sum(nhom_x) / len(danh_sach)
    y = sum(nhom_y) / len(danh_sach)
    
    return x, y


data = [(10, 20), (20, 40), (30, 60)]
print(f"Kết quả: {trung_binh_tuple(data)}")