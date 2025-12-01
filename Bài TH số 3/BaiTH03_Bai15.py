def tao_danh_sach_moi(danh_sach_goc):
    ket_qua = []
    
    for phan_tu in danh_sach_goc:
        
        if phan_tu % 2 == 0 and phan_tu > 10:
            ket_qua.append(phan_tu)
            
    return ket_qua

input_list = [1, 20, 2, 13, -1, 45, -25, 3]
output_list = tao_danh_sach_moi(input_list)

print(f"Gốc: {input_list}")
print(f"Lọc: {output_list}")