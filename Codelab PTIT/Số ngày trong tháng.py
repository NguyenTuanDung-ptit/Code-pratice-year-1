def solution(year, month):
    answer = 0
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            answer = 29
        else:
            answer = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        answer = 30
    else:
        answer = 31
    return answer

# Bạn có thể thêm code ở dưới đây
print(solution(int(input()),int(input())))