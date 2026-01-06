n = int(input())
arr = list(map(int, input("").split()))
print(*arr[::2])
print(*arr[1::2])