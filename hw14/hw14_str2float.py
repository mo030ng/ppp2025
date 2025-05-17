# def str2float(text: str, defalut_value: float = -999) -> float:
#     try: 
#         return float(text)
#     except ValueError:
#         print(f"에러가 낫슴다ㅠㅜㅜ{text}!!")
#         return defalut_value


def is_natural_nums(n):
    return n == int(n) and n > 0 


def natural_num():
    numbers = []

    while True:
        text = input("X=? ")

        try:
            num = int(text)

            if num == -1 :
                break

            if  is_natural_nums(num):
                numbers.append(num)

        except ValueError:
                continue
    return numbers


def main():
    numbers = natural_num()
    print(f"입력된 값은 {numbers} 입니다.")

    count = len(numbers)
    if count > 0 :
        avg = sum(numbers) / len(numbers)
        print(f" 총 {count}개의 자연수가 입력되었고, 평균은 {avg}입니다.")
    else:
        print(f"자연수가 입력되지 않았어요! 다시 시도해주세요. ")



if __name__ == '__main__':
    main()