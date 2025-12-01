def gop_sku_thu_cong(danh_sach):
    kho_tam = {}
    
    for sku, qty in danh_sach:
        kho_tam[sku] = kho_tam.get(sku, 0) + qty
        
    return list(kho_tam.items())

data = [('A01', 10), ('B02', 5), ('A01', 20)]
print(gop_sku_thu_cong(data))