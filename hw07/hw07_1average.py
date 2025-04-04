def average(nums):
    # if len(nums)==0:
    #     return 0
    return sum(nums) / len(nums)

def main():
    nums=[2,6,5,7,8,9,14,1]
    print(f"이 함수들의 평균은 {average(nums)}입니다.")

if __name__=="__main__":
    main()