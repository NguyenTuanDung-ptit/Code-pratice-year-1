import string
from collections import Counter

sentence = input("Nhập một đoạn văn: ")
lower_sentence = sentence.lower()
split_sentence = lower_sentence.split()
split_sentence = [x for x in split_sentence if x not in string.punctuation]
new_sentence = " ".join(split_sentence)
appear = Counter(split_sentence)
dem_so_lan = appear.most_common()
print("Loại bỏ dấu câu:", new_sentence)
print("Danh sách số lần xuất hiện:", dem_so_lan)