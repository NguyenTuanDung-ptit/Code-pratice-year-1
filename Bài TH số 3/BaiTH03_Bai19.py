def tim_cap_gan_nhat_two_pointers(danh_sach, n):
    if len(danh_sach) < 2:
        return None

    danh_sach.sort()
    
    left = 0                   
    right = len(danh_sach) - 1 
    
    min_diff = float('inf')
    best_pair = ()
    
    while left < right:
        current_sum = danh_sach[left] + danh_sach[right]
        
        diff = abs(n - current_sum)
        
        if diff < min_diff:
            min_diff = diff
            best_pair = (danh_sach[left], danh_sach[right])
        
        if current_sum < n:
            left += 1
        elif current_sum > n:
            right -= 1
        else:
            return best_pair, 0
            
    return best_pair, min_diff

data = [10, 5, 20, 30, 4, 1] 
target = 23

cap_so, lech = tim_cap_gan_nhat_two_pointers(data, target)
print(f"Cách 2: Cặp {cap_so} (Tổng {sum(cap_so)}) gần {target} nhất.")
