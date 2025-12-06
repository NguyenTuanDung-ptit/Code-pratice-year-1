while True:
    num = input()
    if int(num) >= 1000 and int(num) <= 9999:
        break

num_sorted = sorted(num)
num_sorted_reverse = num_sorted[::-1]
result = num_sorted_reverse[0] + num_sorted_reverse[1] + num_sorted_reverse[2] + num_sorted_reverse[3]
if int(result) == int(num):
    result = num_sorted[0] + num_sorted[1] + num_sorted[2] + num_sorted[3]
else:
    result = num_sorted_reverse[0] + num_sorted_reverse[1] + num_sorted_reverse[2] + num_sorted_reverse[3]

print(result)