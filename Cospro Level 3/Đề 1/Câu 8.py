while True:
    n = int(input())
    arr = list(map(int, input("").split()))
    if len(arr) != n:
        break
    else:
        max = max(arr) 
        min = min(arr)
        print(max - min)