def read_db(filename):
    temps_list=[]
    rainfall_list=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            tagv=float(tokens[4])
            rainfall=float(tokens[9])
            temps_list.append(tagv)
            rainfall_list.append(rainfall)

    return temps_list,rainfall_list
            
 
def main():
    temps_list,rainfall_list = read_db("hw09/weather(146)_2022-2022 (1).csv")

    t_average= sum(temps_list)/len(temps_list)

    rainfall_over_5 = 0 
    for i in rainfall_list:
        if i >=5:
            rainfall_over_5+=1

    total_rainfall = sum(rainfall_list)

    print(f"연 평균 기온(일평균 기온의 연평균) =>{t_average:.2f}C")
    print(f"5mm이상 강우일수 => {rainfall_over_5}일")
    print(f"총 강우량=>{total_rainfall:.2f}mm")


if __name__=="__main__":
    main()