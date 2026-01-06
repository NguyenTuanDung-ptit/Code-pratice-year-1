n = int(input())
arr = list(map(int, input("").split()))
ds_le = []
ds_chan = []
for i in range(0,n):
    if arr[i] % 2 == 0:
        ds_chan.append(arr[i])
    else:
        ds_le.append(arr[i])
print(*ds_le)
print(*ds_chan)
print(sum(ds_le),sum(ds_chan))