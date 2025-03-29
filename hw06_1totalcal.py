def main():
    print()

if __name__=="__main__":
    main()




fruit = {"샤인머스켓", "천도복숭아", "수박"}
fruit_cal = {"샤인머스켓":66/100 , "천도복숭아":32/100 , "수박":31/100}
fruit_eat = {"샤인머스켓":150, "천도복숭아":200, "수박":100}

total=0
for item in fruit_eat.keys():
    print(item, fruit_cal[item],fruit_eat[item],fruit_cal[item]*fruit_eat[item])
    total+= fruit_cal[item]*fruit_eat[item]

print(f"총 칼로리는 {total:.0f}kcal 입니다.")