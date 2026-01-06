#Tự viết code (Full)
arr = list(map(int, input("").split()))
ds = []
for i in arr:
    if i % 5 == 0:
        ds.append(i)

print(*ds)
sum = sum(ds)
len = len(ds)
average = sum / len
result = round(average, 2)
print(len, sum, result)