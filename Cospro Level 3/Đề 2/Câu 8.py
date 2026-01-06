#Tự viết code (Full)
n = int(input())
arr = tuple(map(int, input("").split()))
for i in range(0, n):
    count = arr.count(i)
    print(count, end = '')