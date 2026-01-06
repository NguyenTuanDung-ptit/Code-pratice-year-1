n = int(input())
if n < 2:
    print("Không phải số nguyên tố")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Số nguyên tố")