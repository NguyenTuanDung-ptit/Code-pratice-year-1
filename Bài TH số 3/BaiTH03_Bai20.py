def xu_ly_ma_tran(matrix):
    n = len(matrix)
    
    tong_chinh = sum(matrix[i][i] for i in range(n))

    tong_phu = sum(matrix[i][n - 1 - i] for i in range(n))
    
    dang_tuple = tuple(tuple(row) for row in matrix)
    
    return tong_chinh, tong_phu, dang_tuple

matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

t_chinh, t_phu, ket_qua_tuple = xu_ly_ma_tran(matrix)

print(f"Tổng chéo chính: {t_chinh}")  
print(f"Tổng chéo phụ:   {t_phu}")    
print(f"Dạng Tuple:      {ket_qua_tuple}")