def main():
    fruit_cal = read_db("./lec/calorie_db.csv")
    fruit_eat = {"쑥":150, "바나나":200}

    total=0
    for item in fruit_eat:
        total+= fruit_cal[item]*fruit_eat[item]
        
    print(f"총 칼로리는 {total:.0f}kcal 입니다.")





def read_db(filename):
    calorie_dic = dict()
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            calorie_dic[tokens[0]] = int(tokens[1])
            print(line)

    return calorie_dic



if __name__=="__main__":
    main()