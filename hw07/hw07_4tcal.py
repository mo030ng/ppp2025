def total_calorie(fruits, fruits_cal_dic):
    total=0
    for item in fruits:
        total += fruits_cal_dic[item]*fruits[item]
    return total


def main():
    fruits = {"샤인머스켓":150, "천도복숭아":200, "수박":100}  
    fruits_cal_dic = {"샤인머스켓":66/100 , "천도복숭아":32/100 , "수박":31/100}
    total= total_calorie(fruits, fruits_cal_dic)
    print(f"총 칼로리는 {total:.0f}kcal 입니다.")


if __name__=="__main__":
    main()