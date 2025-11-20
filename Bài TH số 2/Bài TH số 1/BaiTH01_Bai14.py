import random

problem = random.randint(1, 10)

while True:
    num = int(input("Người dùng xin hãy đoán số 1-10: "))
    if num == problem:
        print("Người dùng đã đoán chính xác.")
        break
    elif num < problem:
        print("Lớn hơn")
    elif num > problem:
        print("Nhỏ hơn")