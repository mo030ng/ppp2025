def read_numbers(filename):
    nums = []
    with open(filename) as f : 
        for line in f:
            nums.append(int(line.strip()))
    return nums

def max(nums):
    sorted_list = sorted(nums)
    return sorted_list[-1]

def min(nums):
    sorted_list = sorted(nums)
    return sorted_list[0]


def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list) // 2]

def main():
    nums = read_numbers("hw08/numbers1.txt")
    print ("주어진 숫자의 개수는",len(nums))
    print ("평균값은 {:.1f}".format(average(nums)))
    print ("최댓값은 {}".format(max(nums)))
    print ("최솟값은 {}".format(min(nums)))
    print ("중앙값은 {}".format(median(nums)))

if __name__=="__main__":
    main()
