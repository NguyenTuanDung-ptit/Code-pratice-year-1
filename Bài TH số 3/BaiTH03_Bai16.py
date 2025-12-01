diem_so = {
    'An': 8.5,
    'Bình': 6.0,
    'Chi': 9.5,
    'Dũng': 7.0
}

danh_sach_da_sap_xep = sorted(diem_so.items(), key=lambda x: x[1], reverse=True)

print(danh_sach_da_sap_xep)
