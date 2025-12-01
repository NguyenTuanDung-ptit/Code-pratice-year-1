from collections import Counter

a = {'tao': 10, 'cam': 20, 'xoai': 5}
b = {'tao': 15, 'dua': 30, 'cam': 5}

c1 = Counter(a)
c2 = Counter(b)

tong = c1 + c2

result = dict(tong)
print(f"Dict mới: {result}")