def solution(text):
    answer = ''
    cnt = [0, 0, 0, 0, 0]
    alpha = ['a', 'e', 'i', 'o', 'u']

    for i in range(0, len(text)):
        if text[i] == 'a':
            cnt[0] += 1
        elif text[i] == 'e':
            cnt[1] += 1
        elif text[i] == 'i':
            cnt[2] += 1
        elif text[i] == 'o':
            cnt[3] += 1
        elif text[i] == 'u':
            cnt[4] += 1

    index = 0
    for i in range(0, 5):
        if cnt[i] > index:
            index = cnt[i]

    answer = alpha[cnt.index(index)]
    
    return answer

if __name__ == "__main__":
    text = input()
    answer = solution(text)
    print(answer)