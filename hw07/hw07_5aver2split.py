def average(nums):
    return sum(nums) / len(nums)

def main():
    text_input = input("숫자들을 입력하세요: ")
    print(text_input)
    print(text_input.split(","))
    nums = [int (x) for x in text_input.split(",")]
    print(nums)
    print(f"이 함수들의 평균은 {average(nums)}입니다.")

if __name__=="__main__":
    main()