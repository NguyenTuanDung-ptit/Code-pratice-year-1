def solution(input_string):
    result = sum(1 for char in input_string if char.isnumeric() == False and char.isalpha() == False)
    return result

def main():
    input_string = input()
    result = solution(input_string)
    print(result)

if __name__ == "__main__":
    main()