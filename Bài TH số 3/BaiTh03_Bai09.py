def xoa(danh_sach_goc):
    ket_qua = []
    
    for phan_tu in danh_sach_goc:
        
        if phan_tu not in ket_qua:
            ket_qua.append(phan_tu)
            
    return ket_qua

input_list = [1, 2, 2, 3, 1, 4, 5, 3]
output_list = xoa(input_list)

print(f"Gốc: {input_list}")
print(f"Lọc: {output_list}")