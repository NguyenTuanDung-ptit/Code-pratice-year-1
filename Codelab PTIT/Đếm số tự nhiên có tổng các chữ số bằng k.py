import math

def cal_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def solution(n, k):
    answer = 0

    for i in range(1, n + 1):
        if cal_sum(i) == k:
            answer += 1

    print(answer)
    return answer
# Bạn có thể thêm code ở dưới đây
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    solution(n, k)